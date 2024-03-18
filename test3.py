#Variables des conditions limites
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

Tl = 0
T0 = 296
L = 3
precDist = 50
precT = int(12*precDist)
D = 1
temps = 1

deltaX2 = (L/precDist)**2
deltaT = temps/precT

def matriceInit(Ti):
    global deltaT, deltaX2, D, precDist

    Tj = []
    Tj.append(Ti[0])
    for i in range(1, precDist):
        Tj.append((D * deltaT * ((Ti[i + 1] - 2 * Ti[i] + Ti[i - 1]) / deltaX2)) + Ti[i])
    Tj.append(Ti[precDist])
    return Tj


Bl = []
for i in range(precDist + 1):
    Bl.append(4 * ((i * L) / precDist) * (3 - ((i * L) / precDist)))

Tj = np.array(Bl)

x = np.linspace(0, L, precDist + 1)

print("Matrice initial : ", Tj)
resultat = matriceInit(Tj)  # Initialize the matrix with Tj
desired_times = []
desired_plot = []
times = []


# Initialize figure and axis for plotting
fig, ax = plt.subplots()

for i in range(precT):
    current_time = i * deltaT
    if current_time in desired_times:
        print("Iteration ", i + 1, " : ", resultat)
        times.append(current_time)
        desired_plot.append(resultat)

    resultat = matriceInit(resultat)  # Update 'resultat' for the next iteration

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
    for i in range(1, len(x)):
        # Define start and end points
        start_x, end_x = x[i - 1], x[i]
        start_y, end_y = data[i - 1], data[i]

        # Normalize the value to get a color
        z = norm([data[i - 1], data[i]])
        color = cmap(z)

        # Plot line segment with gradient
        ax.plot([start_x, end_x], [start_y, end_y], color=color[0])

# Adding labels and legend (adjust as needed)
plt.xlabel('Distance (en m)')
plt.ylabel('Température (en K)')

# Create a colorbar to show the temperature scale
sm = cm.ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])  # You might need this for older matplotlib versions
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label('Température (en K)')

#plt.legend(['t = 0', 't = 0.01', 't = 0.1', 't = 1'])

plt.show()