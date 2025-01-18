import sys
sys.setrecursionlimit(3000)
def init_ruban(taille1, taille2=0):     # taille1 et taille2 représentent les tailles des deux séquences de 1
   # retourne un préfixe de 600 zéros (zones vides au début de la bande), une séquence de size1 1, un séparateur de deux 0, une deuxième séquence de size2 1 (si elle est utilisée), remplit le reste du ruban jusqu'à une longueur totale de 1200 (la longueur du ruban)
   return ([0] * 600) + ([1] * taille1) + ([0] * 2) + ([1] * taille2) + ([0] * (1200 - taille1 - taille2 - 2 - 600))

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

# Fonctions récursives pour les opérations sur listes
def new_len(liste) :  # Calcule la longueur d'une liste de manière récursive
   # Si la liste est vide (if not liste), retourne 0
   # Sinon, retourne 1 (pour l'élément courant) + la longueur du reste de la liste (new_len(liste[1:]))
   if not liste :
       return 0
   return 1 + new_len(liste[1:])

def new_join(liste, index=0, resultat=""):   # Construit une chaîne de caractères représentant les éléments d'une liste, de manière récursive
   # liste : La liste à convertir en chaîne
   # index : Position actuelle dans la liste (initialement 0)
   # resultat : Chaîne accumulée au cours de la récursion
   # Si l'index atteint la longueur de la liste (new_len(liste)), retourne la chaîne construite
   if index == new_len(liste) :
       return resultat
   return new_join(liste, index + 1, resultat + "{}".format(liste[index]))

ruban = [0] * 1200
X = new_len(ruban) // 2

# Initialisation de la première plage de 1
for i in range(3+1) :
  ruban[X+i] = 1
def boucle0():
    D()
    D()
    if ruban[X] == 0 :
        return
    else :
        boucle0()
boucle0()
G()
G()
G()
def boucle1():
    if ruban[X] == 0 :
        return
    else :
        E0()
        G()
        boucle1()
boucle1()
def boucle2():
    D()
    if ruban[X] == 1 :
        return
    else :
        boucle2()
boucle2()

# Extraction de la fenêtre visible du ruban
ruban_visible = new_join(ruban[600-50:600+50])
print(ruban_visible) # Affichage du contenu
# Création de la ligne de marqueur de position
ligne_marqueur_pos = [' '] * 200
ligne_marqueur_pos[X-600+50] = 'X'
ligne_marqueur_pos = new_join(ligne_marqueur_pos)
print(ligne_marqueur_pos) # Affichage de la position
