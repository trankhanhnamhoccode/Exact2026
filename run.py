# Constants
k = 8.9875e9  # Coulomb's constant in N·m²/C²

def e_field(q, charge_pos, target_pos):
    """
    Calculate the electric field vector (Ex, Ey) at target_pos due to a point charge q at charge_pos.
    
    Parameters:
        q (float): Charge value in Coulombs
        charge_pos (tuple): Position of the charge as (x, y)
        target_pos (tuple): Position where the field is calculated as (x, y)
        
    Returns:
        tuple: Electric field vector components (Ex, Ey) in V/m
    """
    
    # Convert charges from nC to C
    q = q * 1e-9
    
    x1, y1 = charge_pos
    x2, y2 = target_pos
    
    r = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5  # Distance between charges
    if r == 0:
        return (0, 0)
    
    Ex = k * q * (x2 - x1) / r**3
    Ey = k * q * (y2 - y1) / r**3
    
    return (Ex, Ey)


# Coordinates setup
A = (-0.03, 0)
B = (0.03, 0)
C = (0, 0.05)  # Point C is 5 cm from A and 3 cm from B

# Charges in Coulombs
q1 = 6e-8
q2 = -6e-8
q3 = 6e-8

# Calculate electric fields due to q1 and q2 at point C
E1 = e_field(q1, A, C)
E2 = e_field(q2, B, C)

# Total electric field vector at point C
Ex_total = E1[0] + E2[0]
Ey_total = E1[1] + E2[1]

# Magnitude of the total electric field
E_total = (Ex_total**2 + Ey_total**2)**0.5

print(f"E_x: {Ex_total:.3f} V/m")
print(f"E_y: {Ey_total:.3f} V/m")
print(f"Total E: {E_total:.3f} V/m")