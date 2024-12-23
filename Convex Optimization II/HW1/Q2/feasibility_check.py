import numpy as np
from scipy.optimize import linprog

C = 100
f = np.array([
    [0.1, 0.8, 0.1],
    [0.5, 0.15, 0.35],
    [0.3, 0.1, 0.6],
    [0.1, 0.9, 0],
    [0.7, 0, 0.3]
])
P = np.array([15, 40, 35, 9, 80])
g = np.array([0.6, 0.3, 0.1])
target = g * C

# Test if linear system can be solved
A_eq = f.T
b_eq = target

print(np.linalg.lstsq(A_eq, b_eq, rcond=None)[0])
