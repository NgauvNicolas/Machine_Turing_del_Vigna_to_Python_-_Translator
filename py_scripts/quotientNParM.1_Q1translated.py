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
# Initialisation de la seconde plage de 1 (séparée par 2 cases)
for i in range(5+1):
    ruban[X+3+3+i] = 1

# Extraction de la fenêtre visible du ruban
ruban_visible = ''.join(map(str,ruban[600-50:600+50]))
print(ruban_visible)  # Affichage du contenu
# Création de la ligne de marqueur de position
ligne_marqueur_pos = [' '] * 200
ligne_marqueur_pos[X-600+50] = 'X'  # Position de la tête
ligne_marqueur_pos = ''.join(ligne_marqueur_pos)
print(ligne_marqueur_pos)  # Affichage de la position

G()
G()
E1()
D()
def boucle0() :
    D()
    if ruban[X] == 0 :
        0
    else :
        boucle0()
boucle0()
def boucle1() :
    D()
    if ruban[X] == 0 :
        0
    else :
        boucle1()
boucle1()
E1()
def boucle2() :
    G()
    if ruban[X] == 0 :
        0
    else :
        boucle2()
boucle2()
D()
D()

# Extraction de la fenêtre visible du ruban
ruban_visible = ''.join(map(str,ruban[600-50:600+50]))
print(ruban_visible)  # Affichage du contenu
# Création de la ligne de marqueur de position
ligne_marqueur_pos = [' '] * 200
ligne_marqueur_pos[X-600+50] = 'X'  # Position de la tête
ligne_marqueur_pos = ''.join(ligne_marqueur_pos)
print(ligne_marqueur_pos)  # Affichage de la position

def boucle3() :
    def boucle4() :
        D()
        if ruban[X] == 0 :
            G()
            0
        else :
            G()
            E0()
            def boucle5() :
                G()
                if ruban[X] == 1 :
                    0
                else :
                    boucle5()
            boucle5()
            G()
            def boucle6() :
                G()
                if ruban[X] == 0 :
                    0
                else :
                    boucle6()
            boucle6()
            D()
            D()
            if ruban[X] == 0 :
                G()
                E0()
                0
            else :
                G()
                E0()
                def boucle7() :
                    D()
                    if ruban[X] == 0 :
                        0
                    else :
                        boucle7()
                boucle7()
                D()
                D()
                def boucle8() :
                    D()
                    if ruban[X] == 1 :
                        0
                    else :
                        boucle8()
                boucle8()
                boucle4()
    boucle4()
    if ruban[X] == 0 :
        0
    else :
        
        # Extraction de la fenêtre visible du ruban
        ruban_visible = ''.join(map(str,ruban[600-50:600+50]))
        print(ruban_visible)  # Affichage du contenu
        # Création de la ligne de marqueur de position
        ligne_marqueur_pos = [' '] * 200
        ligne_marqueur_pos[X-600+50] = 'X'  # Position de la tête
        ligne_marqueur_pos = ''.join(ligne_marqueur_pos)
        print(ligne_marqueur_pos)  # Affichage de la position
        
        def boucle9() :
            G()
            if ruban[X] == 1 :
                0
            else :
                E1()
                boucle9()
        boucle9()
        G()
        def boucle10() :
            G()
            if ruban[X] == 0 :
                0
            else :
                boucle10()
        boucle10()
        def boucle11() :
            G()
            if ruban[X] == 1 :
                0
            else :
                boucle11()
        boucle11()
        def boucle12() :
            G()
            if ruban[X] == 0 :
                0
            else :
                boucle12()
        boucle12()
        E1()
        def boucle13() :
            D()
            if ruban[X] == 0 :
                0
            else :
                boucle13()
        boucle13()
        def boucle14() :
            D()
            if ruban[X] == 1 :
                0
            else :
                boucle14()
        boucle14()
        def boucle15() :
            D()
            if ruban[X] == 0 :
                0
            else :
                boucle15()
        boucle15()
        D()
        D()
        boucle3()
boucle3()

# Extraction de la fenêtre visible du ruban
ruban_visible = ''.join(map(str,ruban[600-50:600+50]))
print(ruban_visible)  # Affichage du contenu
# Création de la ligne de marqueur de position
ligne_marqueur_pos = [' '] * 200
ligne_marqueur_pos[X-600+50] = 'X'  # Position de la tête
ligne_marqueur_pos = ''.join(ligne_marqueur_pos)
print(ligne_marqueur_pos)  # Affichage de la position
