import numpy as np
import scipy as scipy


class Game:
    def __init__(self, density, nbColumns, nbRows):
        # Initialise à None un attribut de classe pour stocker une matrice de cellules en 2D
        [...]

        # Initialise à None un attribut de classe pour stocker une matrice de cellules représentant le nombre de voisins
        # de chaque cellule en 2D
        [...]

        # Initialise une matrice de convolution permettant de calculer le nombre de voisins de chaque cellule
        # Indice : Numpy
        [...]

        # Doit-on compter le point central dans la convolution ? Corrige ce problème
        [...]

        # Créé une fonction permettant de remplir la matrice des cellules aléatoirement en fonction du nombre
        # de colonnes, de lignes et de la densité de cellules vivantes
        self.buildCells(density, nbColumns, nbRows)

    def buildCells(self, density, nbColumns, nbRows):
        # Taille de la matrice : [nbColumns][nbRows]

        # Densité de cellules vivantes : 40(%)
        # Probabilité qu'elle soit vivante : density/100 (0.4)
        # Probabilité qu'elle soit morte : 1 - density/100 (0.6)

        # Cellule vivante = 1, cellule morte = 0
        # Une probabilité est aléatoire donc np.random.choice entre 1 et 0 avec une probabilité de
        # density/100 pour avoir 1, et une probabilité de 1-density/100 pour avoir 0
        [...]

    def clearCells(self, nbColumns, nbRows):
        # Remplissage de la matrice avec des zéros
        [...]

    def compute(self):
        # Utilisation de la librairie scipy pour effectuer la convolution entre chaque cellule et tous ses voisins
        # Stocker le résultat dans la matrice représentant le nombre de voisins
        [...]

    def cycle(self):
        # Compute neighbors for every cell
        self.compute()

        # Iterate through the whole board
        # Pas besoin de connaître les nbCol et nbRow, vous avez déjà la matrice stockée en attribut la classe
        for x in range([...]):
            for y in range([...]):

                # Rule 1: if a cell is living and is surrounded by 2 or 3 living cells, it survives
                [...]

                # Rule 2: if a cell is dead and is surrounded by 3 living cells, it comes back to life
                [...]

                # If no rule is respected, the cell is dead upon the next iteration
                [...]