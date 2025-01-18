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

# Extraction de la fenêtre visible du ruban
ruban_visible = ''.join(map(str,ruban[600-50:600+50]))
print(ruban_visible)  # Affichage du contenu
# Création de la ligne de marqueur de position
ligne_marqueur_pos = [' '] * 200
ligne_marqueur_pos[X-600+50] = 'X'  # Position de la tête
ligne_marqueur_pos = ''.join(ligne_marqueur_pos)
print(ligne_marqueur_pos)  # Affichage de la position

if ruban[X] == 0 :
    sys.exit()
def boucle0() :
    if ruban[X] == 0 :
        0
    else :
        D()
        boucle0()
boucle0()
D()

# Extraction de la fenêtre visible du ruban
ruban_visible = ''.join(map(str,ruban[600-50:600+50]))
print(ruban_visible)  # Affichage du contenu
# Création de la ligne de marqueur de position
ligne_marqueur_pos = [' '] * 200
ligne_marqueur_pos[X-600+50] = 'X'  # Position de la tête
ligne_marqueur_pos = ''.join(ligne_marqueur_pos)
print(ligne_marqueur_pos)  # Affichage de la position

def boucle1() :
    E1()
    def boucle2() :
        G()
        if ruban[X] == 0 :
            0
        else :
            boucle2()
    boucle2()
    def boucle3() :
        G()
        if ruban[X] == 1 :
            0
        else :
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
    
    G()
    if ruban[X] == 0 :
        0
    else :
        D()
        E0()
        def boucle4() :
            D()
            if ruban[X] == 1 :
                0
            else :
                boucle4()
        boucle4()
        def boucle5() :
            D()
            if ruban[X] == 0 :
                0
            else :
                boucle5()
        boucle5()
        boucle1()
boucle1()

# Extraction de la fenêtre visible du ruban
ruban_visible = ''.join(map(str,ruban[600-50:600+50]))
print(ruban_visible)  # Affichage du contenu
# Création de la ligne de marqueur de position
ligne_marqueur_pos = [' '] * 200
ligne_marqueur_pos[X-600+50] = 'X'  # Position de la tête
ligne_marqueur_pos = ''.join(ligne_marqueur_pos)
print(ligne_marqueur_pos)  # Affichage de la position

D()
def boucle6() :
    D()
    if ruban[X] == 1 :
        0
    else :
        E1()
        boucle6()
boucle6()
G()
E0()
D()

# Extraction de la fenêtre visible du ruban
ruban_visible = ''.join(map(str,ruban[600-50:600+50]))
print(ruban_visible)  # Affichage du contenu
# Création de la ligne de marqueur de position
ligne_marqueur_pos = [' '] * 200
ligne_marqueur_pos[X-600+50] = 'X'  # Position de la tête
ligne_marqueur_pos = ''.join(ligne_marqueur_pos)
print(ligne_marqueur_pos)  # Affichage de la position
