# Compte rendu TP2 Calderon-Déchelette

On cherche a simplifier cette équation de la conduction thermique.\
$\frac{{\partial{T}}}{{\partial{t}}}={D}\frac{{\partial^{{2}}{T}}}{{\partial{x}^{{2}}}}$

On se trouve dans un millieu a une dimension homogène et isotrope

## Condition initiales

Au départ, la température du centre est plus élevé que celle des bords.\
On donne T en fonction de t (en seconde) et x (en metre) et L la longueur final\
${T}{\left({x}={0},{t}\right)}={0}$\
${T}{\left({x}={L},{t}\right)}={0}$\
${T}{\left({x},{t}={0}\right)}={4}{x}{\left({3}-{x}\right)}$

## Équation discrétisée

$\lim_{{∆{t}→{0}}}\frac{{⁡{T}^{{{n}+{1}}}_{j}-{T}^{{n}}_{j}}}{\Delta}{t}=\lim_{{{\left(\Delta{x}\right)}^{{2}}→{0}}}⁡{D}\frac{{{T}^{{n}}_{\left({j}+{1}\right)}-{2}{T}^{{n}}_{j}+{T}^{{n}}_{\left({j}-{1}\right)}}}{{{\left(\Delta{x}\right)}^{{2}}}}$\
$\frac{{⁡{T}^{{{n}+{1}}}_{j}-{T}^{{n}}_{j}}}{\Delta}{t}={D}\frac{{{T}^{{n}}_{\left({j}+{1}\right)}-{2}{T}^{{n}}_{j}+{T}^{{n}}_{\left({j}-{1}\right)}}}{{{\left(\Delta{x}\right)}^{{2}}}}$\
$\frac{{⁡{T}^{{{n}+{1}}}_{j}}}{\Delta}{t}={D}\cdot\frac{{{T}^{{n}}_{\left({j}+{1}\right)}-{2}{T}^{{n}}_{j}+{T}^{{n}}_{\left({j}-{1}\right)}}}{{{\left(∆{x}\right)}^{{2}}}}+\frac{{{T}^{{n}}_{j}}}{{\Delta{t}}}$\
$⁡{T}^{{{n}+{1}}}_{j}={D}\cdot\frac{{{T}^{{n}}_{\left({j}+{1}\right)}-{2}{T}^{{n}}_{j}+{T}^{{n}}_{\left({j}-{1}\right)}}}{{{\left(∆{x}\right)}^{{2}}}}+{T}^{{n}}_{j}$

```{=latex}
\begin{center}
```
![](schema_1d_instationnaire.png){width="40%"}

```{=latex}
\end{center}
```
Nous avons employé la bibliothèque matplotlib en Python pour créer une représentation du système.

## résultats

On peut donc grâce à cette simulation calculer des valeurs :

```{=latex}
\begin{center}
```
![](3_courbes.png){width="40%"}

```{=latex}
\end{center}
```
(Discrétisation de temps = 10 000 et de distance de 150)

On peut ensuite générer sur un grand nombre de valeurs:

```{=latex}
\begin{center}
```
![](){width="40%"}

```{=latex}
\end{center}
```
Nous avons sélectionné une discrétisation de 15 points en x et de 50 intervalles de temps, pour t allant de 0 à 1 seconde.

## interpretation et conditions limites

Le rapport maximum de notre systeme est de ${0.5}$ pour $\frac{{{\left.{d}{t}\right.}}}{{\left({\left.{d}{x}\right.}\right)}^{{2}}}$ avec une diffusivité ${1}$\
On vois que la chaleur diminue plutot rapidement au debut puis le vitesse diminution est de plus en plus petite au cour du temps.\
De plus, nous remarquons que la valeur maximale de chaleur demeure constamment localisée au centre du système.

## on comprend pas mais tkt

Pour assurer une précision adéquate, il est essentiel de discrétiser à la fois dans le temps et dans l'espace de manière proportionnelle. Sinon, des écarts significatifs entre les différentes simulations peuvent se produire, entraînant des imprécisions considérables.\
Nous avons ainsi déterminé numériquement qu'avec une valeur donnée de ${N}_{{x}}$, le nombre de pas de temps ${N}_{{t}}$ doit être supérieur à environ ${0.222}$ fois ${N}_{{x}}$ (environ deux neuvièmes de ${N}_{{x}}$) pour obtenir des résultats satisfaisants.

Cas limite : ${N}_{{t}}={0.222}\cdot{{N}_{{x}}^{{2}}}$

Lorsque nous examinons les deltas, nous obtenons l'inégalité suivante :

$ \frac{T_{\text{fin}}}{L} \left( \frac{\Delta t}{\Delta x^2} \right) < 0.5 \Rightarrow \frac{N_t}{N_x} \left( \frac{\Delta x}{\Delta x^2} \right) < 0.5$\
Cette inégalité nous indique que pour obtenir une simulation stable, le rapport entre le nombre de pas de temps ( N_t ) et le nombre de pas d'espace ( N_x ), multiplié par le rapport entre le pas d'espace ( `\Delta `{=tex}x ) et son carré, doit être inférieur à 0.5.

```{=latex}
\begin{center}
```
![](){width="40%"}

```{=latex}
\end{center}
```
