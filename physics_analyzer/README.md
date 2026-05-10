# Physics Problem Analyzer - Chạy trên Kaggle

## 🎯 Giới thiệu
Tool phân loại và trích xuất thông tin bài toán Vật lý sử dụng Ollama và các mô hình Qwen, được thiết kế để chạy trực tiếp trên Kaggle Notebook.

## 🚀 Cách chạy trên Kaggle (3 bước)

### Bước 1: Tải project lên Kaggle
- Tải folder `physics-analyzer` về máy
- Lên [Kaggle](https://www.kaggle.com/) -> Datasets -> New Dataset
- Upload toàn bộ folder lên (kéo thả hoặc chọn file)

### Bước 2: Tạo Notebook mới
- Vào [Kaggle](https://www.kaggle.com/) -> Code -> New Notebook
- Settings -> Accelerator -> Chọn **GPU P100** (quan trọng để chạy nhanh)
- Add Dataset vừa upload vào Notebook (Add Data -> Your Datasets)

### Bước 3: Run Notebook với code bên dưới

Copy toàn bộ code sau vào Notebook và chạy từng cell:

```python
# Cell 1: Di chuyển vào thư mục project
import os
os.chdir('/kaggle/input/physics-analyzer')
print("✅ Đã chuyển vào thư mục:", os.getcwd())

# Cell 2: Cài đặt dependencies
!sudo apt-get update
!sudo apt-get install -y zstd
!pip install ollama pydantic

import subprocess
import time
import json
from pathlib import Path

# Cell 3: Khởi động Ollama server
subprocess.run("pkill ollama", shell=True, stderr=subprocess.DEVNULL)
time.sleep(1)

subprocess.Popen("ollama serve", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(5)
print("✅ Ollama server đã khởi động!")

# Cell 4: Tải models (chạy lần đầu, mất 2-3 phút)
import ollama

print("Đang tải models...")
ollama.pull('qwen3:0.6b')  # 400MB
ollama.pull('qwen3:1.7b')  # 1GB
print("✅ Models đã sẵn sàng!")

# Cell 4: Tải models (chạy lần đầu, mất 2-3 phút)
import ollama

print("Đang tải models...")
ollama.pull('qwen3:0.6b')  # 400MB
ollama.pull('qwen3:1.7b')  # 1GB
print("✅ Models đã sẵn sàng!")

# Cell 5: Import các hàm từ project
from utils import load_prompt, start_ollama_server
from main import classify_with_llm, problem_extracter

# Khởi động server (nếu chưa)
start_ollama_server()

# Cell 6: Test với các câu hỏi mẫu
test_questions = [
    "Calculate the energy stored in capacitor C when C = 100 μF and U = 30 V.",
    "Based on the premises, what can we conclude about the curriculum? A. It enhances engagement B. It needs more resources",
    "A 5 kg block on a frictionless 30° incline is connected to a 3 kg hanging mass. Find acceleration."
]

print("="*60)
print("🧪 KIỂM TRA PHÂN LOẠI CÂU HỎI")
print("="*60)

for q in test_questions:
    print(f"\n📝 Câu hỏi: {q[:60]}...")
    try:
        result = classify_with_llm(q)
        print(f"   🔍 Loại: {result['qtype']}")
    except Exception as e:
        print(f"   ❌ Lỗi: {e}")

        ⚠️ Xử lý lỗi
Lỗi "Ollama not found":
Chạy lại cell 2 và 3

Lỗi "Out of memory":

Vào Settings -> Chọn GPU nhẹ hơn hoặc tắt GPU

Lỗi "File not found":

Kiểm tra lại đường dẫn trong cell 1

