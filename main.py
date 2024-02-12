import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm


temperature=296
n=999
main_diag = np.eye(n) * -2
upper_diag = np.eye(n, k=1)
lower_diag = np.eye(n, k=-1)
mat = main_diag + upper_diag + lower_diag
mat[0] = [1]+[0] * (n-1)
mat[n-1] = [0] * (n-1) + [1]
print(mat)
               

left = np.array([[temperature if i == 0 else 0 for i in range(n)]]).transpose()

print(left)
x = np.linalg.solve(mat, left)

print("x = ")
print(x, end="\n\n")

# Normalize the temperatures to the range [0, 1]
norm = plt.Normalize(x.min(), x.max())

# Create a color map for the temperatures
colors = cm.plasma(norm(x))
fig, ax = plt.subplots()  # Create a new figure and axes
plt.scatter(range(n), x, color=colors, s=10)
plt.xlabel('Temps')
plt.ylabel('Temperature')
plt.title('Temperature Distribution')
cbar = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cm.plasma), ax=ax)  # Specify the axes for the Colorbar
cbar.set_label('Temperature')

plt.show()

# print("ax = ")
# # left = mat * [[t0],[t1],[t2],[t3],[t4],[t5],[t6]]

# print(np.fix(np.matmul(mat, x)))
