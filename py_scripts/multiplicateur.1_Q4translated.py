import sys
sys.setrecursionlimit(3000)


def init_ruban(parametres) :     # taille1 et taille2 représentent les tailles des deux séquences de 1
   taille1 = parametres[0]
   taille2 = parametres[1] if len(parametres) > 1 else 0
   # retourne un préfixe de 600 zéros (zones vides au début de la bande), une séquence de taille1 1, un séparateur de deux 0, une deuxième séquence de taille2 1 (si elle est utilisée), remplit le reste du ruban jusqu'à une longueur totale de 1200 (la longueur du ruban)
   return ([0] * 600) + ([1] * taille1) + ([0] * 2) + ([1] * taille2) + ([0] * (1200 - taille1 - taille2 - 2 - 600))


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

def boucle1():
    D(X)
    if ruban[X[-1]] == 1 :
        return
    else :
        boucle1()
    
boucle1()

def boucle2():
    D(X)
    if ruban[X[-1]] == 0 :
        return
    else :
        boucle2()
    
boucle2()

D(X)
E1()
G(X)
def boucle3():
    G(X)
    if ruban[X[-1]] == 0 :
        return
    else :
        boucle3()
    
boucle3()

def boucle4():
    G(X)
    if ruban[X[-1]] == 1 :
        return
    else :
        boucle4()
    
boucle4()

def boucle5():
    E0()
    G(X)
    if ruban[X[-1]] == 0 :
        return
    else :
        D(X)
        def boucle6():
            D(X)
            if ruban[X[-1]] == 1 :
                return
            else :
                boucle6()
            
        boucle6()
        
        def boucle7():
            D(X)
            if ruban[X[-1]] == 0 :
                return
            else :
                boucle7()
            
        boucle7()
        
        G(X)
        def boucle8():
            E0()
            G(X)
            if ruban[X[-1]] == 0 :
                return
            else :
                D(X)
                def boucle9():
                    D(X)
                    if ruban[X[-1]] == 1 :
                        return
                    else :
                        boucle9()
                    
                boucle9()
                
                def boucle10():
                    D(X)
                    if ruban[X[-1]] == 0 :
                        return
                    else :
                        boucle10()
                    
                boucle10()
                
                E1()
                def boucle11():
                    G(X)
                    if ruban[X[-1]] == 0 :
                        return
                    else :
                        boucle11()
                    
                boucle11()
                
                def boucle12():
                    G(X)
                    if ruban[X[-1]] == 1 :
                        return
                    else :
                        boucle12()
                    
                boucle12()
                
                boucle8()
            
        boucle8()
        
        D(X)
        E1()
        def boucle13():
            D(X)
            if ruban[X[-1]] == 1 :
                return
            else :
                boucle13()
            
        boucle13()
        
        G(X)
        def boucle14():
            G(X)
            if ruban[X[-1]] == 1 :
                return
            else :
                E1()
                boucle14()
            
        boucle14()
        
        def boucle15():
            G(X)
            if ruban[X[-1]] == 1 :
                return
            else :
                boucle15()
            
        boucle15()
        
        boucle5()
    
boucle5()

def boucle16():
    D(X)
    if ruban[X[-1]] == 1 :
        return
    else :
        boucle16()
    
boucle16()

def boucle17():
    E0()
    D(X)
    if ruban[X[-1]] == 0 :
        return
    else :
        boucle17()
    
boucle17()

D(X)
# Extraction de la fenêtre visible du ruban
print(join_v2(ruban[600-50:600+50]))
# Création de la ligne de marqueur de position
print(join_v2([' ']*(X[-1]-600+50) + ['X'] + [' ']*(200-(X[-1]-600+50)-1)))
