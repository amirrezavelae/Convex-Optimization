import cvxpy as cp
import numpy as np

# Given parameters
C = 100

# Matrix of the composition of the alloy
f = np.array([
    [0.1, 0.8, 0.1],
    [0.5, 0.15, 0.35],
    [0.3, 0.1, 0.6],
    [0.1, 0.9, 0],
    [0.7, 0, 0.3]
])

# Vector of the price of the alloy
P = np.array([15, 40, 35, 9, 80])

# Vector of desired composition percentages
g = np.array([0.6, 0.3, 0.1])

# Variables
x = cp.Variable(5)

# Define the objective
objective = cp.Minimize(P @ x)

# Constraints
constraints = [
    cp.sum(x) == C,
    x.T @ f == g * C,
    # x >= 0
]

# Problem definition
problem = cp.Problem(objective, constraints)

# Solve the problem
problem.solve(solver=cp.SCS)


# Output the results
print("Relaxing the non-negativity constraint")
print("Status:", problem.status)
print("Optimal value of x:", x.value)
print("Optimal cost:", problem.value)


# Constraints
constraints = [
    cp.sum(x) == C,
    x.T @ f == g * C,
    x >= 0
]

# Problem definition
problem = cp.Problem(objective, constraints)

# Solve the problem
problem.solve(solver=cp.SCS)


# Output the results
print()
print("="*50)
print("Adding the non-negativity constraint")
print("Status:", problem.status)
print("Optimal value of x:", x.value)
print("Optimal cost:", problem.value)
