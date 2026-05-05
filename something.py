import sympy as sp
import json
import os
import sys
import re

# ==============================================
# Load FORMULA_STORE từ file Python
# ==============================================
def load_formula_store(filepath: str) -> dict:
    """
    Import FORMULA_STORE từ file .py.
    """
    abs_path = os.path.abspath(filepath)
    dir_name = os.path.dirname(abs_path)
    module_name = os.path.splitext(os.path.basename(abs_path))[0]

    if dir_name not in sys.path:
        sys.path.insert(0, dir_name)

    mod = __import__(module_name)
    if not hasattr(mod, 'FORMULA_STORE'):
        raise ValueError(f"Không tìm thấy FORMULA_STORE trong {filepath}")
    return mod.FORMULA_STORE


# ==============================================
# Cốt lõi: giải một phương trình khi biết một số giá trị
# ==============================================
def solve_for(formula_eq: sp.Eq, known: dict, find: str):
    """
    formula_eq: phương trình SymPy, vd Eq(v, u + a*t)
    known: dict ánh xạ tên biến -> giá trị (số hoặc SymPy)
    find: tên của ký hiệu cần tìm (phải có trong formula_eq)
    Trả về giá trị (số hoặc biểu thức).
    """
    all_syms = {str(s): s for s in formula_eq.free_symbols}
    if find not in all_syms:
        raise ValueError(f"Biến '{find}' không có trong công thức.")
    target = all_syms[find]

    known_sym = {}
    for k, v in known.items():
        if k not in all_syms:
            raise ValueError(f"Biến '{k}' không tồn tại trong công thức.")
        known_sym[all_syms[k]] = v

    result = sp.solve(formula_eq.subs(known_sym), target)
    if len(result) == 0:
        raise ValueError("Không thể giải được.")
    return result[0] if len(result) == 1 else result


# ==============================================
# Xử lý từng bước (step)
# ==============================================
def execute_step(step: dict, context: dict, formula_store: dict):
    """
    Thực thi một step, cập nhật context với giá trị tìm được.
    Trả về giá trị mới tính.
    """
    tool = step['tool']
    inputs = step['inputs']
    output_var = step['output']

    # --- Trường hợp đặc biệt: sum (có thể mở rộng thêm) ---
    if tool == 'sum':
        expr_str = list(inputs.values())[0]  # Ví dụ "s1 + s2"
        # Thay thế tên biến bằng giá trị từ context
        for name, val in context.items():
            if isinstance(val, (int, float, sp.Number)):
                expr_str = re.sub(r'\b' + re.escape(name) + r'\b', str(val), expr_str)
        # Tính biểu thức
        try:
            result = sp.sympify(expr_str)
            if result.is_number:
                result = float(result)
        except Exception as e:
            raise RuntimeError(f"Không thể tính toán biểu thức '{expr_str}': {e}")
        context[output_var] = result
        print(f"  [sum] {output_var} = {result}")
        return result

    # --- Dùng công thức từ FORMULA_STORE ---
    # Tìm công thức theo tool id
    formula_entry = None
    for domain, formulas in formula_store.items():
        for f in formulas:
            if f.get('id') == tool:
                formula_entry = f
                break
        if formula_entry:
            break

    if not formula_entry:
        raise ValueError(f"Không tìm thấy công thức có id='{tool}'")

    equation_str = formula_entry['equation']
    variables = formula_entry['variables']

    # Tạo namespace cho eval phương trình (chứa các symbol và hàm)
    namespace = {
        'Eq': sp.Eq,
        'sqrt': sp.sqrt,
        'cos': sp.cos,
        'sin': sp.sin,
        'tan': sp.tan,
        'pi': sp.pi,
        'Rational': sp.Rational,
        'sp': sp,
    }
    # Thêm các symbol từ danh sách biến
    for var in variables:
        namespace[var] = sp.Symbol(var)

    # Parse phương trình
    try:
        eq = eval(equation_str, {"__builtins__": {}}, namespace)
    except Exception as e:
        raise RuntimeError(f"Lỗi parse công thức '{equation_str}': {e}")

    # Xác định ký hiệu cần tìm trong công thức
    # Tìm trong inputs key nào có value (string) trùng với output_var
    symbol_to_find = None
    for sym_name, val in inputs.items():
        if isinstance(val, str) and val == output_var:
            symbol_to_find = sym_name
            break
    if not symbol_to_find:
        # Nếu không có mapping, ta thử dùng chính output_var nếu nó có trong công thức
        if output_var in variables:
            symbol_to_find = output_var
        else:
            raise ValueError(f"Không thể ánh xạ output '{output_var}' vào biến nào trong công thức {variables}")

    # Chuẩn bị known: thay thế các biến đã biết trong công thức
    known = {}
    for sym_name, val in inputs.items():
        if sym_name == symbol_to_find:
            continue  # đây là ẩn số, bỏ qua
        if isinstance(val, str):
            # val là tên biến trong context
            if val not in context:
                raise ValueError(f"Biến '{val}' chưa được tính toán trước đó")
            known[sym_name] = context[val]
        else:
            # val là số
            known[sym_name] = val

    # Bổ sung thêm: nếu trong công thức có biến đã biết trong context mà chưa có trong inputs
    for var in variables:
        if var not in known and var in context:
            known[var] = context[var]

    # Gọi solve_for để tìm symbol_to_find
    result = solve_for(eq, known, find=symbol_to_find)

    # Chuyển về số nếu có thể
    if isinstance(result, sp.Number):
        result_val = float(result)
    elif isinstance(result, sp.Basic) and result.is_number:
        result_val = float(result)
    else:
        result_val = result  # có thể là biểu thức còn chứa ký hiệu

    # Lưu vào context với tên output_var (tên thực tế của biến trong bài toán)
    context[output_var] = result_val
    print(f"  [{tool}] {output_var} = {result_val}")
    return result_val


# ==============================================
# Chạy toàn bộ bài toán và cập nhật JSON
# ==============================================
def process_problem(input_file: str, formula_file: str, update_json: bool = False):
    """
    Đọc input.json, chạy các bước, in kết quả.
    Nếu update_json=True, ghi lại giá trị đã tính vào file.
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        problem = json.load(f)

    formula_store = load_formula_store(formula_file)

    context = {}

    # Đưa các giá trị đã biết từ "given" vào context
    for item in problem.get('given', []):
        sym = item['symbol']
        val = item['value']
        if val is not None:
            context[sym] = val

    # Thực hiện từng bước
    steps = problem.get('steps', [])
    for step in steps:
        step_num = step.get('step', '?')
        print(f"\n--- Step {step_num} ---")
        try:
            val = execute_step(step, context, formula_store)
            # Cập nhật lại step value (tuỳ chọn)
            step['value'] = val
        except Exception as e:
            print(f"Lỗi: {e}")
            step['value'] = None

    # Cập nhật các unknown
    for unk in problem.get('unknown', []):
        sym = unk['symbol']
        if sym in context:
            unk['value'] = context[sym]
    # In kết quả cuối cùng
    print("\n===== KẾT QUẢ SAU KHI GIẢI =====")
    for unk in problem.get('unknown', []):
        sym = unk['symbol']
        val = unk.get('value')
        unit = unk.get('unit', '')
        if val is not None:
            print(f"{unk['name']} ({sym}) = {val} {unit}")
        else:
            print(f"{unk['name']} ({sym}) = chưa xác định")

    # Ghi lại file nếu cần
    if update_json:
        with open(input_file, 'w', encoding='utf-8') as f:
            json.dump(problem, f, indent=2, ensure_ascii=False)
        print(f"\nĐã cập nhật file '{input_file}' với các giá trị mới.")

    return context


# ==============================================
# Chạy từ dòng lệnh
# ==============================================
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Physics Solver Helper')
    parser.add_argument('input', help='File input.json')
    parser.add_argument('formula', help='File FORMULA.py')
    parser.add_argument('--update', action='store_true', help='Cập nhật file input.json với giá trị đã tính')
    args = parser.parse_args()

    process_problem(args.input, args.formula, update_json=args.update)