V0.4
05/08/2025

Objectif :
=======

Développer une version simplifiée du jeu frogger pour apprendre à coder en Python.
Ce readme décrit les objectifs, étape par étape, sous forme de petits exercices,
qui mis bout à bout permettre l'implémentation du jeu.

Le jeu Frogger d'origine est visible ici:
https://youtu.be/WNrz9_Fe-Us?si=ePeFyPqV2BQgNWEy

Il y a 4 zones dans frogger.
1. La zone de départ 
2. La route, où les véhicules peuvent écraser la grenouille 
3. La rivière, où la grenouille doit sauter sur des troncs
4. La zone d'arrivée, composée de 5 maisons.

Dans la version simplifiée nous feront:
1. La zone de départ
2. La route
3. La zone d'arrivée

La zone de départ:
------------------------------
On peut s'y déplacer librement sans risque. On est bloqué par les bords droit et gauche.
On peut y rentrer et sortir autant qu'on le veut.

La zone d'arrivée :
-----------------------------
Il n'y a pas de maison.
Dès qu'on y rentre, on a gagné.

La route :
---------------
Elle est composée de 4 bandes horizontales sur laquelle circulent des véhicules.
Sur une bande, les véhicules circulent tous dans la même direction et à la même vitesse.
Mais vitesse et direction peuvent être différentes d'une bande à l'autre.

Principe:
-------------
La grenouille apparaît dans la zone de départ.

Elle peut se déplacer dans toutes les directions.

Si la grenouille touche un véhicule, elle meurt.

Si elle atteint la zone de d'arrivée on a gagné.

Sur chaque ligne, le sens et la vitesse, de la ligne est choisi aléatoirement au démarrage.
Tous les véhicules d'une même ligne iront dans ce sens et à cette vitesse.

Sur une ligne, les véhicules apparaissent aléatoirement.
La fréquence moyenne d'apparition est également réglable et définie aléatoirement au démarrage.


Étape 1: Image de fond
=======

Le but est de créer le premier programme,
D'importer la bibliothèque pygame,
D'initialiser pygame
D'afficher une image de la route à 4 bande + départ + arrivée 
D'attendre 5 secondes et de quitter.

L'image doit être horizontale, la bande du haut étant l'arrivée, celle du bas le départ, et entre les deux 4 bandes représentant la route.

Etape 2 : Afficher la grenouille
========

Nous allons afficher la grenouille au bas de l'écran sur la bande de départ.
Elle doit être positionnée approximativement au milieu.
L'image de la grenouille doit être orientée vers le haut

Etape 3 : Deplacement de la grenouille
========

Il faut gérer les évenements pygame pour quitter le jeu proprement.
Nous allons donc créer une boucle principale infinie, qui depend d'une variable de type booléen.
Lorsque nous recevons un évenement pygame indiquand qu'on veut quitter le jeu, alors nous changeons la valeur du booléen pour que la boucle se termine.

Nous allons également gérer l'appui sur l'écran tactile.
4 zones seront définies:
1. la bande du haut (la ligne d'arrivée)
2. la bande du bas (la ligne de départ)
3. la moitié gauche de l'écran, excluant les zone 1 et 2
4. la moitié droite de l'écran, excluant les zone 1 et 2

Nous devons donc détecter sur quelle zone le joueur clique, puis agir en conséquence en deplaçant le sprite (l'image) de la grenouille:
1 -> monter
2 -> descendre
3 -> aller à gauche
4 -> aller à droite

La grenouille ne doit jamais sortir de l'écran, même partiellement

Etape 4: Responsivness
=========

Un affichage "responsive" est un affichage qui s'adapte à la taille de l'écran.

Ainsi nous voulons:
1. que le fond occupe la totalité de l'écran
2. que la taille du sprite de la grenouille dépende de la taille de l'écran.
Toujours la hauteur d'une bande (route, zone de depart...)
3. Que la grenouille se deplace d'une distance dépendant de la taille de l'écran:
toujours d'une bande à la verticale, toujours d'un vingtieme de la largeur de l'écran
4. Que la grenouille apparaisse toujours approximativement à la moitié de la bande de départ.

Pour cela nous allons commencer par faire un schéma de l'écran et nous allons y placer les élements suivants:
a. les coordonnées (0,0) en haut à gauche de l'écran.
b. sw (screen width) et sh (screen height) à la fois comme dimensions et comme coordonnées
c. lh (line height), ainsi que 2*lh, 3*lh et LINES*lh
d. cw (column width), ainsi que 2*cw, 3*cw et COLS*cw
e. la position initiale de la grenouille (les coordonnées de son point superieur gauche), le rectangle délimitant le sprite de la grenouille
f. fw (frog width), fh (frog height), et les coordonnées du point inférieur droit du sprite de la grenouille en fonction de xf, yf, (coordonnées courantes de la grenouille) , et fw et fh
g. positionner la grengouille proche de chacun des bords et calculer la distance maximale (ou minimale) à partir de laquelle il faut interdire un déplacement

Modifiez le code pour utiliser les valeurs indiquées dans le schéma pour chacune des initialisations ou des tests.

Etape 5 : rationnalisation
=======

Quand on developpe un programme, il est important de regrouper le code.
C'est utile pour le code qui est réutilisé plusieurs fois dans le programme.
Ca évite de dupliquer le code et de gaspiller de l'espace, mais ça évite aussi de devoir appliquer d'éventuelles corrections à chaque occurence du code dupliqué.
L'autre utilité est pour simplifier la lecture du code. Si une portion de code est complexe, on a intérêt à la séparée.
Pour cela, on va utiliser une fonction, qu'on va définir au début de notre programme, puis qu'on va appeler là où le code origine apparaissait.
Il est ainsi plus facile de lire le code qui appelle la fonction.
On ne se souci plus de la complexité du code de la fonction, ni à le comprendre à chaque lecture, mais on sait simplement l'idée génerale de ce que fait la fonction.
On peut par exemple imaginer une fonction qui prend en entrées les coordonnées de la grenouille et les coordonnées de l'endroit pressé par le joueur sur l'écran tactile, et cette fonction se charge de mettre à jour les coordonnées de la grenouille, en prenant soin de caculer la direction voulue par le joueur et les limites du bord de l'écran.
Mais à la lecture du code qui appelle cette fonction, même si on se souvient qu'elle fait tous ces calculs, on n'a pas besoin de se souvenir des détails.

5.1: Définir cette fonction move_frog qui prend en entrée:
----------------------------------------------------------
- fx, (l'abscisse de la grenouille)
- fy, (l'ordonnée de la grenouille)
- la direction

et qui renvoie:
- les nouvelles coordonnées fx, fy

La fonction doit utiliser un match / case sur la direction.

Pour cela, nous allons définir une énumération, c'est à dire une liste de valeur possible:
On commence par ajouter la ligne suivante au début du programme:
    from enum import IntEnum
Ensuite nous allons définir une énumération "D" avec nos constantes:
class D(IntEnum):
    NONE = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

Pour utiliser ces constantes, il suffira d'appeler
    D.NONE
pour avoir la valeur 0


5.2: Définir une fonction event_manager qui gère les évenements.
--------------------------------------------------
 Elle ne prend aucun paramètre en entrée et renvoie la nouvelle valeur de 'running' et une 'direction' (D.NONE si l'écran n'est pas pressé).

 5.3: Appeler ces deux fonctions
 -------------------------------
 Maintenant que ces deux fonctions sont définies, on peut les appeler dans la boucle principale,
 pour obtenir le même résultat qu'avant, mais avec un code beaucoup plus lisible.
 La dernière étape dz la boucle principame doit être la mise à jour de l'affichage (fond et grenouille)
 
 Etape 6: les véhicules
 =======
 
 Pour cette étape nous voulons afficher les voitures sur les 4 bandes représentant les routes.
Nous voulons que les routes aient chacune:
- un dessin de voiture différente
- un sens (vers la droite ou vers la gauche) qui lui est propre
- une vitesse de déplacement des véhicules qui lui est propre (la même pour toutes les véhicules de la ligne)
- une fréquence moyenne d'apparition des véhicule qui lui est propre (donc différentes pour les autres bandes)


6.1: un véhicule
------
Nous allons afficher un véhicule se déplaçant sur une route.
a. il faut donc charger une image de véhicule
b. il faut redimensionner l'image à la hauteur d'une ligne en conservant l'aspect de l'image.
c. Stocker ses coordonnées dans vx et vy
d. l'afficher aux coordonnées vx et vy dans la boucle principale

6.2: deplacement d'un véhicule
------

Nous allons créer une fonction qui va déplacer notre véhicule.
Pour cela, nous allons:
a. créer une fonction move_car qui prend en entrée:
- vx
- vy
- la direction D.RIGHT ou D.LEFT
- la vitesse (un entier)

6.?: Utiliser un Dict pour définir la route.
-------

Nous allons créer une représentation d'une route, en y notant tous les éléments qui la caractérise:
- son numéro, "nu", de 1 à 4
- le "sprite"" de la voiture à utiliser
- la direction "dir" de valeur D.LEFT ou D.RIGHT
- la vitesse "speed", un entier
- la frequence "freq", un entier
