import numpy as np
import scipy as scipy


class Game:
    def __init__(self, density, nbColumns, nbRows):
        # A vous de définir le stockage des cellules

        self.buildCells(density, nbColumns, nbRows)

    def buildCells(self, density, nbColumns, nbRows):
        # Initialiser aléatoirement la matrice 2D des cellules avec density% de cellules vivantes, et le reste mortes

    def clearCells(self, nbColumns, nbRows):
        # Vider la matrice 2D en tuant toutes les cellules

    def compute(self):
        # Calculer le nombre de voisins de chaque cellule

    def cycle(self):
        # Compute neighbors for every cell
        self.compute()

        # Iterate through the whole board

        # Rule 1: if a cell is living and is surrounded by 2 or 3 living cells, it survives

        # Rule 2: if a cell is dead and is surrounded by 3 living cells, it comes back to life

        # If no rule is respected, the cell is dead upon the next iteration
