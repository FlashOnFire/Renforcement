import numpy as np

mat = np.array([[1, 0, 0, 0, 0, 0, 0],
                [1, -2, 1, 0, 0, 0, 0],
                [0, 1, -2, 1, 0, 0, 0],
                [0, 0, 1, -2, 1, 0, 0],
                [0, 0, 0, 1, -2, 1, 0],
                [0, 0, 0, 0, 1, -2, 1],
                [0, 0, 0, 0, 0, 0, 1], ])
left = np.array([[296], [0], [0], [0], [0], [0], [0]])
x = np.linalg.solve(mat, left)

print("x = ")
print(x, end="\n\n")

print("ax = ")
# left = mat * [[t0],[t1],[t2],[t3],[t4],[t5],[t6]]

print(np.fix(np.matmul(mat, x)))
