import sys
sys.setrecursionlimit(3000)
def init_ruban(taille1, taille2=0):     # taille1 et taille2 représentent les tailles des deux séquences de 1
   # retourne un préfixe de 600 zéros (zones vides au début de la bande), une séquence de taille1 1, un séparateur de deux 0, une deuxième séquence de taille2 1 (si elle est utilisée), remplit le reste du ruban jusqu'à une longueur totale de 1200 (la longueur du ruban)
   return ([0] * 600) + ([1] * taille1) + ([0] * 2) + ([1] * taille2) + ([0] * (1200 - taille1 - taille2 - 2 - 600))

# X[-1] : position actuelle de la tête sur le ruban (dernier élément de la liste X)
def E0(ruban, X) :     # Écriture d'un 0 à la position courante
    ruban.pop(X[-1])
    ruban.insert(X[-1], 0)

def E1(ruban, X) :     # Écriture d'un 1 à la position courante
    ruban.pop(X[-1])
    ruban.insert(X[-1], 1)

def D(X) :     # Déplacement de la tête vers la droite
    X.append(X[-1]+1)
    X.pop(0)

def G(X) :     # Déplacement de la tête vers la gauche
    X.append(X[-1]-1)
    X.pop(0)

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

# Initialisation de la première plage de 1
ruban = init_ruban(int(sys.argv[1])+1, 0)
X = [new_len(ruban) // 2]
try :
    def boucle0(ruban, X):
        D(X)
        D(X)
        if ruban[X[-1]] == 0 :
            return
        else :
            boucle0(ruban, X)
    boucle0(ruban, X)
    G(X)
    G(X)
    G(X)
    def boucle1(ruban, X):
        if ruban[X[-1]] == 0 :
            return
        else :
            E0(ruban, X)
            G(X)
            boucle1(ruban, X)
    boucle1(ruban, X)
    def boucle2(ruban, X):
        D(X)
        if ruban[X[-1]] == 1 :
            return
        else :
            boucle2(ruban, X)
    boucle2(ruban, X)
    
    # Extraction de la fenêtre visible du ruban
    print(new_join(ruban[600-50:600+50]))
    # Création de la ligne de marqueur de position
    print(new_join([' ']*(X[-1]-600+50) + ['X'] + [' ']*(200-(X[-1]-600+50)-1)))
    
except IndexError :
    print('Longueur maximale du ruban atteint à la fin : le programme arrête')
    sys.exit(1)