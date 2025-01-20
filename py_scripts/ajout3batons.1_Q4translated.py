import sys
sys.setrecursionlimit(3000)


def init_ruban(parametres=[0,0]) :     # parametres[0] et parametres[1] représentent les tailles des deux séquences de 1
   # retourne un préfixe de 600 zéros (zones vides au début de la bande), une séquence de parametres[0] 1, un séparateur de deux 0, une deuxième séquence de parametres[1] 1 (si elle est utilisée), remplit le reste du ruban jusqu'à une longueur totale de 1200 (la longueur du ruban)
   return ([0] * 600) + ([1] * parametres[0]) + ([0] * 2) + ([1] * parametres[1]) + ([0] * (1200 - parametres[0] - parametres[1] - 2 - 600))


# X[-1] : position actuelle de la tête sur le ruban (dernier élément de la liste X)
def E0() :     # Écriture d'un 0 à la position courante
    ruban.pop(X[-1])
    ruban.insert(X[-1], 0)
def E1() :     # Écriture d'un 1 à la position courante
    ruban.pop(X[-1])
    ruban.insert(X[-1], 1)

def D(X) :     # Déplacement de la tête vers la droite
    X.append(X[-1]+1)
    X.pop(0)
def G(X) :     # Déplacement de la tête vers la gauche
    X.append(X[-1]-1)
    X.pop(0)


# Fonctions récursives pour les opérations sur listes
def len_v2(liste) :  # Calcule la longueur d'une liste de manière récursive
   # Si la liste est vide (if not liste), retourne 0
   # Sinon, retourne 1 (pour l'élément courant) + la longueur du reste de la liste (len_v2(liste[1:]))
   if not liste :
       return 0
   return 1 + len_v2(liste[1:])

def join_v2(liste) :   # Construit une chaîne de caractères représentant les éléments d'une liste, de manière récursive
   # liste : La liste à convertir en chaîne
   # indice : Position actuelle dans la liste (initialement 0)
   # Si l'indice atteint la longueur de la liste (len_v2(liste)), retourne la chaîne construite
   def join_recc(indice) :
       if indice == len_v2(liste) :
           return ""
       return "{}".format(liste[indice]) + join_recc(indice + 1)
   return join_recc(0)


# Initialisation de deux plages successives de 1 sur le ruban, respectivement de taille int(sys.argv[1])+1 et int(sys.argv[2])+1) ici, et séparées par 2 cases
ruban = init_ruban([int(sys.argv[1])+1, int(sys.argv[2])+1])
X = [len_v2(ruban) // 2]


# Extraction de la fenêtre visible du ruban
print(join_v2(ruban[600-50:600+50]))
# Création de la ligne de marqueur de position
print(join_v2([' ']*(X[-1]-600+50) + ['X'] + [' ']*(200-(X[-1]-600+50)-1)))

def boucle0():
    if ruban[X[-1]] == 0 :
        return
    else :
        D(X)
        boucle0()
    
boucle0()

E1()
D(X)
E1()
D(X)
E1()
# Extraction de la fenêtre visible du ruban
print(join_v2(ruban[600-50:600+50]))
# Création de la ligne de marqueur de position
print(join_v2([' ']*(X[-1]-600+50) + ['X'] + [' ']*(200-(X[-1]-600+50)-1)))
