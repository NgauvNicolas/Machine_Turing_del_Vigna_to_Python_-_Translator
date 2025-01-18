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

nb_etapes = 21
G()
E1()
G()
E1()
G()
E0()
G()
E1()
G()
E1()
def boucle0() :
    E0()
    G()
    E1()
    G()
    E1()
    def boucle1() :
        D()
        D()
        if ruban[X] == 1 :
            0
        else :
            boucle1()
    boucle1()
    E0()
    D()
    E1()
    D()
    E1()
    def boucle2() :
        G()
        G()
        if ruban[X] == 1 :
            0
        else :
            boucle2()
    boucle2()
    
    # Extraction de la fenêtre visible du ruban
    ruban_visible = ''.join(map(str,ruban[600-50:600+50]))
    print(ruban_visible)  # Affichage du contenu
    # Création de la ligne de marqueur de position
    ligne_marqueur_pos = [' '] * 200
    ligne_marqueur_pos[X-600+50] = 'X'  # Position de la tête
    ligne_marqueur_pos = ''.join(ligne_marqueur_pos)
    print(ligne_marqueur_pos)  # Affichage de la position
    
    global nb_etapes
    if nb_etapes > 0 : 
         input('Appuyez sur la touche Entrée pour continuer')
         nb_etapes -= 1
         boucle0()
    else :
         sys.exit()
    boucle0()
boucle0()