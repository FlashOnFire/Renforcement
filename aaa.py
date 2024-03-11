Bl = []
for i in range(precDist + 1):
    Bl.append(4 * ((i * L) / precDist) * (3 - ((i * L) / precDist)))

Tj = np.array(Bl)

x = np.linspace(0, L, precDist + 1)

print("Matrice initial : ", Tj)
resultat = matriceInit(Tj)
for i in range(precT):
    print("Itération ", i + 1, " : ", resultat)
    plt.plot(x, resultat)
    resultat = matriceInit(resultat)

# Tracer la fonction
plt.plot(x, resultat)
# Ajouter des étiquettes pour les axes x et y
plt.xlabel('x')
plt.ylabel('y')

# Afficher le graphique
plt.show()