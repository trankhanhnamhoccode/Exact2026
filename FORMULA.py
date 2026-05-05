FORMULA_STORE = {
    "electricity": [
        {
            "id": "ohms_law",
            "name": "Ohm's Law",
            "use": "Calculate one of V, I, R from the other two",
            "type": "formula",
            "equation": "Eq(V, I * R)",
            "variables": [
                "V",
                "I",
                "R"
            ],
            "keywords": [
                "ohm",
                "current",
                "voltage",
                "resistance",
                "V",
                "I",
                "R"
            ]
        },
        {
            "id": "power_law",
            "name": "Joule–Lenz / Power Law",
            "use": "Calculate power P from V and I (or equivalent forms)",
            "type": "formula",
            "equation": "Eq(P, V * I)",
            "variables": [
                "P",
                "V",
                "I"
            ],
            "keywords": [
                "power",
                "watt",
                "P",
                "V",
                "I"
            ]
        },
        {
            "id": "series_resistance",
            "name": "Resistors in Series",
            "use": "Find total resistance for resistors connected in series",
            "type": "formula",
            "equation": "Eq(R_total, R1 + R2)",
            "variables": [
                "R_total",
                "R1",
                "R2"
            ],
            "keywords": [
                "series",
                "total resistance",
                "R_total",
                "connected in series"
            ]
        },
        {
            "id": "parallel_resistance",
            "name": "Resistors in Parallel",
            "use": "Find total resistance for resistors connected in parallel",
            "type": "formula",
            "equation": "Eq(1/R_total, 1/R1 + 1/R2)",
            "variables": [
                "R_total",
                "R1",
                "R2"
            ],
            "keywords": [
                "parallel",
                "total resistance",
                "R_total",
                "connected in parallel"
            ]
        },
        {
            "id": "capacitor_energy",
            "name": "Energy stored in a capacitor",
            "use": "Calculate energy E from capacitance C and voltage U",
            "type": "formula",
            "equation": "Eq(E, 0.5 * C * U**2)",
            "variables": [
                "E",
                "C",
                "U"
            ],
            "keywords": [
                "capacitor",
                "energy",
                "E",
                "C",
                "U",
                "voltage"
            ]
        },
        {
            "id": "coulomb_force",
            "name": "Coulomb's Law",
            "use": "Calculate electrostatic force between two point charges",
            "type": "formula",
            "equation": "Eq(F, k * q1 * q2 / r**2)",
            "variables": [
                "F",
                "k",
                "q1",
                "q2",
                "r"
            ],
            "keywords": [
                "coulomb",
                "force",
                "charge",
                "electrostatic",
                "F",
                "q",
                "r"
            ]
        },
        {
            "id": "current_division",
            "name": "Current Divider Rule",
            "use": "Find current through a branch in a parallel circuit",
            "type": "formula",
            "equation": "Eq(I_x, I_total * (R_total / R_x))",
            "variables": [
                "I_x",
                "I_total",
                "R_total",
                "R_x"
            ],
            "keywords": [
                "current division",
                "parallel",
                "current",
                "branch"
            ]
        },
        {
            "id": "voltage_division",
            "name": "Voltage Divider Rule",
            "use": "Find voltage across a resistor in a series circuit",
            "type": "formula",
            "equation": "Eq(V_x, V_total * (R_x / R_total))",
            "variables": [
                "V_x",
                "V_total",
                "R_x",
                "R_total"
            ],
            "keywords": [
                "voltage division",
                "series",
                "voltage",
                "resistor"
            ]
        },
        {
            "id": "electric_power_alternate",
            "name": "Power (alternate forms)",
            "use": "Calculate power using P = I^2 R or P = V^2 / R",
            "type": "formula",
            "equation": "Eq(P, I**2 * R)",
            "variables": [
                "P",
                "I",
                "R"
            ],
            "keywords": [
                "power",
                "I^2 R",
                "Joule heating",
                "P",
                "I",
                "R"
            ]
        }
        # Note: power_law already covers P=V*I; we might add the other forms as separate relations.
        # Chúng ta có thể thêm các dạng khác của công suất vào cùng một quan hệ bằng cách sử dụng một hàm linh hoạt, 
        # nhưng để embedding dễ dàng, ta nên tách chúng ra.
    ],
    "kinematics": [
        {
            "id": "velocity_acceleration_time",
            "name": "v = u + at",
            "use": "Calculate final velocity v from initial velocity u, acceleration a, and time t",
            "type": "formula",
            "equation": "Eq(v, u + a*t)",
            "variables": [
                "v",
                "u",
                "a",
                "t"
            ],
            "keywords": [
                "velocity",
                "acceleration",
                "time",
                "motion",
                "v",
                "u",
                "a",
                "t"
            ]
        },
        {
            "id": "displacement_uvt",
            "name": "s = (u + v)t / 2",
            "use": "Calculate displacement s from initial and final velocities and time",
            "type": "formula",
            "equation": "Eq(s, (u + v) * t / 2)",
            "variables": [
                "s",
                "u",
                "v",
                "t"
            ],
            "keywords": [
                "displacement",
                "initial velocity",
                "s",
                "u",
                "v",
                "t",
                "final velocity",
                "distance"
            ]
        },
        {
            "id": "displacement_ut_half_at2",
            "name": "s = ut + ½at²",
            "use": "Calculate displacement s from initial velocity, acceleration, and time",
            "type": "formula",
            "equation": "Eq(s, u*t + 0.5*a*t**2)",
            "variables": [
                "s",
                "u",
                "a",
                "t"
            ],
            "keywords": [
                "displacement",
                "acceleration",
                "time",
                "s",
                "u",
                "a",
                "t",
                "distance"
            ]
        },
        {
            "id": "velocity_squared",
            "name": "v² = u² + 2as",
            "use": "Relate velocities, acceleration, and displacement",
            "type": "formula",
            "equation": "Eq(v**2, u**2 + 2*a*s)",
            "variables": [
                "v",
                "u",
                "a",
                "s"
            ],
            "keywords": [
                "velocity squared",
                "displacement",
                "acceleration",
                "v^2",
                "u^2"
            ]
        },
        {
            "id": "average_speed",
            "name": "Average speed",
            "use": "Calculate average speed from total distance and total time",
            "type": "formula",
            "equation": "Eq(v_avg, s_total / t_total)",
            "variables": [
                "v_avg",
                "s_total",
                "t_total"
            ],
            "keywords": [
                "average speed",
                "total distance",
                "total time",
                "v_avg"
            ]
        },
        {
            "id": "shm_period_angular_freq",
            "name": "T = 2π/ω",
            "use": "Relate period T and angular frequency ω in SHM",
            "type": "formula",
            "equation": "Eq(T, 2*pi/omega)",
            "variables": [
                "T",
                "omega",
                "pi"
            ],
            "keywords": [
                "period",
                "angular frequency",
                "SHM",
                "T",
                "omega",
                "pi"
            ]
        },
        {
            "id": "shm_frequency_period",
            "name": "f = 1/T",
            "use": "Relate frequency f and period T",
            "type": "formula",
            "equation": "Eq(f, 1/T)",
            "variables": [
                "f",
                "T"
            ],
            "keywords": [
                "frequency",
                "period",
                "SHM",
                "f",
                "T"
            ]
        },
        {
            "id": "shm_max_speed",
            "name": "v_max = ωA",
            "use": "Calculate maximum speed in SHM from amplitude A and angular frequency ω",
            "type": "formula",
            "equation": "Eq(v_max, omega * A)",
            "variables": [
                "v_max",
                "omega",
                "A"
            ],
            "keywords": [
                "maximum speed",
                "SHM",
                "amplitude",
                "angular frequency",
                "v_max",
                "omega",
                "A"
            ]
        },
        {
            "id": "shm_max_acceleration",
            "name": "a_max = ω²A",
            "use": "Calculate maximum acceleration in SHM",
            "type": "formula",
            "equation": "Eq(a_max, omega**2 * A)",
            "variables": [
                "a_max",
                "omega",
                "A"
            ],
            "keywords": [
                "maximum acceleration",
                "SHM",
                "a_max",
                "omega",
                "A"
            ]
        }
    ],
    "dynamics": [
        {
            "id": "newton2",
            "name": "Newton's Second Law",
            "use": "Calculate net force F from mass m and acceleration a",
            "type": "formula",
            "equation": "Eq(F_net, m * a)",
            "variables": [
                "F_net",
                "m",
                "a"
            ],
            "keywords": [
                "newton",
                "force",
                "mass",
                "acceleration",
                "F",
                "m",
                "a"
            ]
        },
        {
            "id": "weight",
            "name": "Weight",
            "use": "Calculate weight W from mass m and gravity g",
            "type": "formula",
            "equation": "Eq(W, m * g)",
            "variables": [
                "W",
                "m",
                "g"
            ],
            "keywords": [
                "weight",
                "gravity",
                "W",
                "m",
                "g"
            ]
        },
        {
            "id": "friction_kinetic",
            "name": "Kinetic Friction",
            "use": "Calculate kinetic friction force f_k from normal force N and coefficient μ_k",
            "type": "formula",
            "equation": "Eq(f_k, mu_k * N)",
            "variables": [
                "f_k",
                "mu_k",
                "N"
            ],
            "keywords": [
                "friction",
                "kinetic",
                "f_k",
                "mu_k",
                "N"
            ]
        },
        {
            "id": "friction_static_max",
            "name": "Maximum Static Friction",
            "use": "Calculate maximum static friction force f_s_max",
            "type": "formula",
            "equation": "Eq(f_s_max, mu_s * N)",
            "variables": [
                "f_s_max",
                "mu_s",
                "N"
            ],
            "keywords": [
                "static friction",
                "maximum",
                "f_s_max",
                "mu_s",
                "N"
            ]
        },
        {
            "id": "gravity_force",
            "name": "Newton's Law of Gravitation",
            "use": "Calculate gravitational force between two masses",
            "type": "formula",
            "equation": "Eq(F, G * m1 * m2 / r**2)",
            "variables": [
                "F",
                "G",
                "m1",
                "m2",
                "r"
            ],
            "keywords": [
                "gravity",
                "gravitational force",
                "F",
                "G",
                "m1",
                "m2",
                "r"
            ]
        },
        {
            "id": "spring_force",
            "name": "Hooke's Law",
            "use": "Calculate spring force from spring constant k and displacement x",
            "type": "formula",
            "equation": "Eq(F, -k * x)",
            "variables": [
                "F",
                "k",
                "x"
            ],
            "keywords": [
                "spring",
                "Hooke",
                "force",
                "k",
                "x"
            ]
        },
        {
            "id": "momentum",
            "name": "Momentum",
            "use": "Calculate momentum p from mass m and velocity v",
            "type": "formula",
            "equation": "Eq(p, m * v)",
            "variables": [
                "p",
                "m",
                "v"
            ],
            "keywords": [
                "momentum",
                "p",
                "m",
                "v"
            ]
        },
        {
            "id": "impulse",
            "name": "Impulse-Momentum Theorem",
            "use": "Relate impulse to change in momentum",
            "type": "formula",
            "equation": "Eq(F_avg * delta_t, m * (v_f - v_i))",
            "variables": [
                "F_avg",
                "delta_t",
                "m",
                "v_f",
                "v_i"
            ],
            "keywords": [
                "impulse",
                "momentum",
                "force",
                "time"
            ]
        },
        {
            "id": "work_constant_force",
            "name": "Work done by constant force",
            "use": "Calculate work W from force F, displacement s, and angle θ",
            "type": "formula",
            "equation": "Eq(W, F * s * cos(theta))",
            "variables": [
                "W",
                "F",
                "s",
                "theta"
            ],
            "keywords": [
                "work",
                "force",
                "displacement",
                "angle",
                "W"
            ]
        },
        {
            "id": "kinetic_energy",
            "name": "Kinetic Energy",
            "use": "Calculate kinetic energy KE from mass m and velocity v",
            "type": "formula",
            "equation": "Eq(KE, 0.5 * m * v**2)",
            "variables": [
                "KE",
                "m",
                "v"
            ],
            "keywords": [
                "kinetic energy",
                "KE",
                "m",
                "v"
            ]
        },
        {
            "id": "potential_energy_gravity",
            "name": "Gravitational Potential Energy",
            "use": "Calculate PE from mass m, gravity g, and height h",
            "type": "formula",
            "equation": "Eq(PE, m * g * h)",
            "variables": [
                "PE",
                "m",
                "g",
                "h"
            ],
            "keywords": [
                "potential energy",
                "gravity",
                "height",
                "PE",
                "m",
                "g",
                "h"
            ]
        },
        {
            "id": "power_work_time",
            "name": "Power (work/time)",
            "use": "Calculate power P from work W and time t",
            "type": "formula",
            "equation": "Eq(P, W / t)",
            "variables": [
                "P",
                "W",
                "t"
            ],
            "keywords": [
                "power",
                "work",
                "time",
                "P",
                "W",
                "t"
            ]
        }
    ],
    "thermodynamics": [
        {
            "id": "heat_transfer",
            "name": "Heat Transfer (Q=mcΔT)",
            "use": "Calculate heat Q from mass m, specific heat c, and temperature change ΔT",
            "type": "formula",
            "equation": "Eq(Q, m * c * (T_f - T_i))",
            "variables": [
                "Q",
                "m",
                "c",
                "T_f",
                "T_i"
            ],
            "keywords": [
                "heat",
                "specific heat",
                "temperature",
                "Q",
                "m",
                "c",
                "T"
            ]
        },
        {
            "id": "latent_heat",
            "name": "Latent Heat",
            "use": "Calculate heat Q for phase change from mass m and latent heat L",
            "type": "formula",
            "equation": "Eq(Q, m * L)",
            "variables": [
                "Q",
                "m",
                "L"
            ],
            "keywords": [
                "latent heat",
                "phase change",
                "Q",
                "m",
                "L"
            ]
        },
        {
            "id": "thermal_equilibrium",
            "name": "Thermal Equilibrium (no phase change)",
            "use": "Find final temperature when two substances reach thermal equilibrium",
            "type": "theory",
            "equation": "Eq(m1 * c1 * (T_f - T1) + m2 * c2 * (T_f - T2), 0)",
            "variables": [
                "m1",
                "c1",
                "T1",
                "m2",
                "c2",
                "T2",
                "T_f"
            ],
            "keywords": [
                "thermal equilibrium",
                "calorimetry",
                "final temperature",
                "mixing"
            ]
        },
        {
            "id": "ideal_gas_law",
            "name": "Ideal Gas Law",
            "use": "Relate pressure P, volume V, amount n, and temperature T for an ideal gas",
            "type": "formula",
            "equation": "Eq(P * V, n * R * T)",
            "variables": [
                "P",
                "V",
                "n",
                "R",
                "T"
            ],
            "keywords": [
                "ideal gas",
                "pressure",
                "volume",
                "moles",
                "temperature",
                "R"
            ]
        }
    ]
    
}