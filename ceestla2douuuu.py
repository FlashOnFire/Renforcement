import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

Tl = 0
T0 = 296
L = 3
precDist = 30
precT = 3#int(12*precDist)
D = 1
temps = 1

deltaX2 = (L/precDist)**2
deltaY2 = (L/precDist)**2
deltaT = temps/precT

def matriceInit2D(Ti):
    global deltaT, deltaX2, deltaY2, D, precDist

    Tj = np.zeros((precDist+1, precDist+1))

    for i in range(1, precDist):
        for j in range(1, precDist):
            Tj[i, j] = (D * deltaT * ((Ti[i + 1, j] - 2 * Ti[i, j] + Ti[i - 1, j]) / deltaX2 + (Ti[i, j + 1] - 2 * Ti[i, j] + Ti[i, j - 1]) / deltaY2)) + Ti[i, j]

    return Tj

Bl = np.zeros((precDist+1, precDist+1))
for i in range(precDist + 1):
    for j in range(precDist + 1):
        Bl[i, j] = 4 * ((i * L) / precDist) * (3 - ((j * L) / precDist))

Tj = np.array(Bl)

x = np.linspace(0, L, precDist + 1)
y = np.linspace(0, L, precDist + 1)

print("Matrice initial : ", Tj)
resultat = matriceInit2D(Tj)  # Initialize the matrix with Tj
desired_times = []
desired_plot = []
times = []

for i in range(precT):
    current_time = i * deltaT
    if current_time in desired_times:
        print("Iteration ", i + 1, " : ", resultat)
        times.append(current_time)
        desired_plot.append(resultat)

    resultat = matriceInit2D(resultat)  # Update 'resultat' for the next iteration

    # Update the boundary conditions
    resultat[0, :] = Tj[0, :]
    resultat[:, 0] = Tj[:, 0]
    resultat[-1, :] = Tj[-1, :]
    resultat[:, -1] = Tj[:, -1]

#plot the last iteration
desired_plot.append(resultat)
times.append(temps)

# Compute global min and max for the color normalization
all_values = np.concatenate(desired_plot)
min_val, max_val = all_values.min(), all_values.max()
norm = colors.Normalize(vmin=min_val, vmax=max_val)
cmap = cm.plasma

# Initialize figure and axis for plotting
fig, ax = plt.subplots()

# Plot gradient lines
for data, time in zip(desired_plot, times):
    ax.imshow(data, cmap=cmap, norm=norm)

# Adding labels and legend (adjust as needed)
plt.xlabel('Distance (en m)')
plt.ylabel('Distance (en m)')

# Create a colorbar to show the temperature scale
sm = cm.ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])  # You might need this for older matplotlib versions
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label('Température (en K)')

plt.show()