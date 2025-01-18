import sys

# Initialisation du ruban avec 1200 cases à 0
ruban = [0] * 1200
X = len(ruban) // 2

def E0() :
    ruban[X] = 0  # Écriture d'un 0 à la position courante

def E1() :
    ruban[X] = 1  # Écriture d'un 1 à la position courante

def D() :
    global X
    X += 1 # Déplacement de la tête vers la droite

def G() :
    global X
    X -= 1 # Déplacement de la tête vers la gauche

# Initialisation de la première plage de 1
for i in range(3+1):
  ruban[X+i] = 1
def boucle0() :
    boucle0()
boucle0()