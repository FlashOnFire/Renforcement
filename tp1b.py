import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm

temperature = 296.0
distance = 3
n = 50
# (4x*(3-x)*296)
main_diag = np.eye(n) * -2
upper_diag = np.eye(n, k=1)
lower_diag = np.eye(n, k=-1)
mat = main_diag + upper_diag + lower_diag
mat[0] = [1] + [0] * (n - 1)
mat[n - 1] = [0] * (n - 1) + [1]
print(mat)

left_array = [0.1 * (1 / 1000)*4 * (x * (3 / n)) * (3 - (x * (3 / n))) * temperature for x in range(n)]
arrays = [left_array]

for i in range(10):
    left_array = np.linalg.solve(mat, left_array)
    left_array = [0.1*x for x in left_array]
    # left_array = [0.1*4*(x*(3/(n-1)))*(3-(x*(3/(n-1)))) for x in left_array]
    arrays.append(left_array)

arrays = [np.array(x, dtype=np.float64) for x in arrays]

# Create a color map for the temperatures
fig, ax = plt.subplots()  # Create a new figure and axes

i = 3

x = arrays[i]
norm = plt.Normalize(x.min(), x.max())
colors = cm.plasma(norm(x))
plt.scatter(np.linspace(0, distance, n), x, color=colors, s=10)

plt.xlabel('Distance (mètres)')
plt.ylabel('Temperature (Kelvin)')
plt.title('Temperature Distribution')
cbar = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cm.plasma), ax=ax)  # Specify the axes for the Colorbar
cbar.set_label('Temperature (Kelvin)')

plt.show()

# print("ax = ")
# # left = mat * [[t0],[t1],[t2],[t3],[t4],[t5],[t6]]

# print(np.fix(np.matmul(mat, x)))
