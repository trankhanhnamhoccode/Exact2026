import numpy as np

k = 9e9  # hằng số Coulomb

def electric_field(charges, target):
    """
    charges: list of (q, position_vector)
    target: position vector
    """
    E = np.array([0.0, 0.0])

    for q, pos in charges:
        r_vec = target - pos
        r = np.linalg.norm(r_vec)

        if r == 0:
            continue

        # vector Coulomb: r_vec / |r|^3
        E += k * q * r_vec / (r ** 3)

    return E


# Ví dụ 1: thẳng hàng trên trục x
charges = [
    (1e-6, np.array([0.0, 0.0])),
]

target = np.array([2.0, 0.0])

E = electric_field(charges, target)

print("Electric field:", E)
print("Magnitude:", np.linalg.norm(E))