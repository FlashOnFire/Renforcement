import numpy as np

n=9999
main_diag = np.eye(n) * -2
upper_diag = np.eye(n, k=1)
lower_diag = np.eye(n, k=-1)
mat = main_diag + upper_diag + lower_diag
mat[0] = [1]+[0] * (n-1)
mat[n-1] = [0] * (n-1) + [1]
print(mat)
               

left = np.array([[296 if i == 0 else 0 for i in range(n)]]).transpose()

print(left)
x = np.linalg.solve(mat, left)

print("x = ")
print(x, end="\n\n")

print("ax = ")
# left = mat * [[t0],[t1],[t2],[t3],[t4],[t5],[t6]]

print(np.fix(np.matmul(mat, x)))
