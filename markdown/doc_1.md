# Compte rendu Guillaume Calderon - Eymeric Déchelette

## Détermination de la formule

Nous sommes partis de l'équation de la chaleur : $\frac{{\partial\phi}}{{\partial{t}}}+\nabla\cdot{\left(\phi{V}\right)}={S}$

### Méthode analytique

Nous avons commencé par simplifier l'expression :\
Tout d'abord, nous avons considéré que l'objet ne bougeait pas, et également qu'il était uniforme.\
Nous avons ensuite supposé qu'aucune source de chaleur active n'existait.

### Méthode numérique

Au précedent cours, nous avions simplifié l'équation de la chaleur par : $\frac{{{d}^{{2}}{T}}}{{{\left.{d}{x}\right.}^{{2}}}}={0}$\
On sait que $\frac{{{d}{T}}}{{{\left.{d}{x}\right.}}}=\lim_{{{x}\to{a}}}\frac{{{T}{\left({x}+{a}\right)}-{T}{\left({a}\right)}}}{{{x}-{a}}}=\lim_{{{x}\to}}\frac{{{T}{\left({x}\right)}-{T}{\left({a}\right)}}}{{\Delta{x}}}$\
Nous obtenons donc : $\frac{{{d}^{{2}}{T}}}{{{\left.{d}{x}\right.}^{{2}}}}=\lim_{{{x}\to{0}}}{\left(\lim_{{{x}\to{0}}}\frac{{{T}_{{{j}+{1}}}-{T}_{{j}}}}{{\Delta{x}}}\right)}\frac{{{T}_{{j}}-{T}_{{{j}-{1}}}}}{{\Delta{x}}}$\
Ainsi : $\frac{{{d}^{{2}}{T}}}{{{\left.{d}{x}\right.}^{{2}}}}=\lim_{{{x}\to{0}}}\frac{{{T}_{{{j}-{1}}}-{2}{T}_{{j}}+{T}_{{{j}+{1}}}}}{{\left(\Delta{x}\right)}^{{2}}}={0}$

## Détermination de la matrice

Avec la formule précente : $\frac{{{d}^{{2}}{T}}}{{{\left.{d}{x}\right.}^{{2}}}}=\lim_{{{x}\to{0}}}\frac{{{T}_{{{j}-{1}}}-{2}{T}_{{j}}+{T}_{{{j}+{1}}}}}{{\left(\Delta{x}\right)}^{{2}}}={0}$,\
On peut déduire que sous forme matricielle cela s'écrit : ${\left(\begin{array}{c} {296}\\{0}\\\vdots\\{0}\end{array}\right)}={\left(\begin{array}{ccccc} {1}&{0}&{0}&\ldots&{0}\\{1}&-{2}&{1}&\ddots&\vdots\\{0}&\ddots&\ddots&\ddots&\ddots\\\vdots&\ddots&{1}&-{2}&{1}\\{0}&\ldots&{0}&{0}&{1}\end{array}\right)}{\left(\begin{array}{c} {T}_{{0}}\\\vdots\\{T}_{{n}}\end{array}\right)}$

Il ne nous reste plus qu'à résoudre le système matriciel à l'aide de python.\
On peut également simplement choisir la présision de notre résolution en choisissant la valeur de n.

Après simulation numérique, on obtient la courbe :

```{=latex}
\begin{center}
```
![](Figure_1.png){width="60%"}

```{=latex}
\end{center}
```
## Conditions limites :

Nous obtenons bien ${T}_{{0}}={296.0}$ (température initiale)\
et ${T}_{{n}}={0}$

Les conditions aux limites sont donc respectées
