# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as alg
from mpl_toolkits.mplot3d import axes3d


j = np.linspace(0, 3, 6)
n = np.linspace(0, 3, 6)
Nx = 100
v = np.linspace(0, 3, Nx + 1)
dx = 3 / Nx
dt = 1 / (10 * Nx)
# A =np.array([[1, 0, 0, 0, 0, 0], [1/dx, -2/dx, 1/dx, 0, 0, 0], [0, 1/dx, -2/dx, 1/dx, 0, 0], [0, 0, 1/dx, -2/dx, 1/dx, 0], [0, 0, 0, 1/dx, -2/dx, 1/dx], [0, 0, 0, 0, 0, 1]])
# b = np.array([[295], [0], [0], [0], [0], [0]])
# Tj=alg.solve(A, b)
# plt.plot(x, Tj)
# plt.xlabel('Longueur (m)')
# plt.ylabel('Température (K)')
# plt.show()

# T =np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
T = np.zeros((10 * Nx + 1, Nx + 1))
print(T)
for k in range(1, Nx):  # initialisation conditions initiales
    T[0][k] = 4 * (k * dx) * (3 - (k * dx))

for i in range(1, 10 * Nx + 1):
    for j in range(1, Nx):
        T[i][j] = (dt * (T[i - 1][j + 1] - 2 * T[i - 1][j] + T[i - 1][j - 1]) / (dx) ** 2) + T[i - 1][j]

print(T)
# for l in range(0,10*Nx, int(Nx*10/4)):
for l in [0, 1, 10, 10 * Nx]:
    plt.plot(v, T[l], label=dt * l)
    plt.xlabel('Longueur (m)')
    plt.ylabel('Température (K)')
plt.title('dx={dx} dt={dt} Nx={Nx}'.format(dx=dx, dt=dt, Nx=Nx))
plt.legend()
plt.show()
print(T[0])
print(T[10])
print(T[10 * Nx])

theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)  # Création du tableau de l'axe z entre -2 et 2
r = z ** 2 + 1
x = r * np.sin(theta)  # Création du tableau de l'axe x
y = r * np.cos(theta)  # Création du tableau de l'axe y

# Tracé du résultat en 3D
fig = plt.figure()
ax = fig.gca(projection='3d')  # Affichage en 3D
ax.plot(x, y, z, label='Courbe')  # Tracé de la courbe 3D
plt.title("zwip zwip")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.tight_layout()
plt.show()

dy = 3 / Nx
w = np.linspace(0, 3, 10 * Nx + 1)
T = np.zeros((Nx + 1, 10 * Nx + 1, 10 * Nx + 1))
print(T)
for k in range(1, 10 * Nx):  # initialisation conditions initiales
    for l in range(1, 10 * Nx):
        T[0][l][k] = 0

for k in range(1, 10 * Nx):  # initialisation conditions initiales
    for l in range(1, Nx):
        T[l][0][k] = 1

for i in range(1, Nx):
    for j in range(1, 10 * Nx):
        for k in range(1, 10 * Nx):
            T[i][j][k] = (dt * (((T[i - 1][j + 1][k] - 2 * T[i - 1][j][k] + T[i - 1][j - 1][k]) / (dx) ** 2) + (
                        (T[i - 1][j][k + 1] - 2 * T[i - 1][j][k] + T[i - 1][j][k - 1]) / (dy) ** 2))) + T[i - 1][j][k]

print(T)
# for l in range(0,10*Nx, int(Nx*10/4)):
fig = plt.figure()
# ax = fig.gca(projection='3d')
for l in [0, 1, 10, Nx]:
    for k in [0, 1, 10, Nx]:
        # Affichage en 3D

        # ax.plot(v, T[k][l], T[l][k], label='Courbe')
        print('T', T[k])

        plt.contourf(w, w, T[k])  # Tracé de la courbe 3D

# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
plt.tight_layout()
plt.colorbar()
plt.title('dx={dx}=dy dt={dt} Nx={Nx}'.format(dx=dx, dt=dt, Nx=Nx))
plt.legend()
plt.show()
print(T[0][0])
print(T[10][10])
print(T[Nx][Nx])


