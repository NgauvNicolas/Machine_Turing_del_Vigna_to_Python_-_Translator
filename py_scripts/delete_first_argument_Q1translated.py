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

if ruban[X] == 0 :
    
    # Extraction de la fenêtre visible du ruban
    ruban_visible = ''.join(map(str,ruban[600-50:600+50]))
    print(ruban_visible)  # Affichage du contenu
    # Création de la ligne de marqueur de position
    ligne_marqueur_pos = [' '] * 200
    ligne_marqueur_pos[X-600+50] = 'X'  # Position de la tête
    ligne_marqueur_pos = ''.join(ligne_marqueur_pos)
    print(ligne_marqueur_pos)  # Affichage de la position
    
    sys.exit()
if ruban[X] == 1 :
    D()
    
    # Extraction de la fenêtre visible du ruban
    ruban_visible = ''.join(map(str,ruban[600-50:600+50]))
    print(ruban_visible)  # Affichage du contenu
    # Création de la ligne de marqueur de position
    ligne_marqueur_pos = [' '] * 200
    ligne_marqueur_pos[X-600+50] = 'X'  # Position de la tête
    ligne_marqueur_pos = ''.join(ligne_marqueur_pos)
    print(ligne_marqueur_pos)  # Affichage de la position
    
    def boucle0() :
        if ruban[X] == 0 :
            0
        else :
            if ruban[X] == 1 :
                E0()
                
                # Extraction de la fenêtre visible du ruban
                ruban_visible = ''.join(map(str,ruban[600-50:600+50]))
                print(ruban_visible)  # Affichage du contenu
                # Création de la ligne de marqueur de position
                ligne_marqueur_pos = [' '] * 200
                ligne_marqueur_pos[X-600+50] = 'X'  # Position de la tête
                ligne_marqueur_pos = ''.join(ligne_marqueur_pos)
                print(ligne_marqueur_pos)  # Affichage de la position
                
                D()
                
                # Extraction de la fenêtre visible du ruban
                ruban_visible = ''.join(map(str,ruban[600-50:600+50]))
                print(ruban_visible)  # Affichage du contenu
                # Création de la ligne de marqueur de position
                ligne_marqueur_pos = [' '] * 200
                ligne_marqueur_pos[X-600+50] = 'X'  # Position de la tête
                ligne_marqueur_pos = ''.join(ligne_marqueur_pos)
                print(ligne_marqueur_pos)  # Affichage de la position
                
                boucle0()
    boucle0()
    def boucle1() :
        if ruban[X] == 0 :
            G()
            if ruban[X] == 1 :
                0
            else :
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
    