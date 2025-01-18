"""
Question II.
Instruction for : utilisation de la récursivité pour les conditions et boucles.


Exemple d'appel en ligne de commande sur le terminal : python traducteur_q2.py ts_scripts/multiplicateur.1.TS 3 5
    Et on obtient le Script Python généré : py_scripts/multiplicateur.1_Q2translated.py
On peut ensuite tester le Script Python qui a été créé à partir de la traduction du Script TS :
    Exemple d'appel en ligne de commande sur le terminal : python py_scripts/multiplicateur.1_Q2translated.py
    On note qu'il n'y a ici pas besoin d'arguments pour l'exécution du script généré, puisque les arguments qu'on veut utiliser on été prise en compte lors de la création de ce script à la commande précédente.
        
De manière générale, adapter le nombre d'arguments lors de la génération du script python en fonction de la tâche à effectuer ensuite 
    (si c'est une multiplication, une addition ou une division par exemple, alors il faut 2 arguments de valeurs à manipuler, 
    mais dans d'autres tâches ce n'est pas forcément nécessaire, par exemple avec ajout3batons.1.TS on peut utiliser 1 seul argument et avec 01.1.TS aucun argument).
"""



import sys


# Classe principale assurant la traduction d'un script MTdV vers un sous-ensemble Python comme stipulé dans l'énoncé
class MTdV_Traducteur_q2 :
    def __init__(self) :
        """
        Initialise les variables dont on a besoin pour la traduction.
        """
        # Indentation courante
        self.indentation_courante = 0
        
        # Compteur pour compter les boucles afin de les nommer et les différencier selon les étapes
        self.boucle_valeur_max = 0
        # Compteur pour la position courante des boucles
        self.boucle_position_courante = 0
        # Stocke les noms des boucles, leur position et leur indentation
        self.boucle_nom_pos_ind = []

        # Compteurs pour conditions
        self.if_compteur = 0
        self.else_compteur = 0

        # Stockage du code généré
        self.code = []

    def indentation(self) :
        """
        Gère l'indentation selon self.indentation_courante afin de respecter le niveau d'imbrication.
        """
        return "    " * self.indentation_courante

    def ajouter_ligne(self, ligne) :
        """
        Ajoute une ligne de code correctement indentée.
        """
        self.code.append(self.indentation() + ligne)

    def generer_entete(self) :
        """
        Génère l'en-tête du programme Python avec :
        - L'initialisation du ruban (liste de 1200 cases)
        - La position initiale de la tête (au milieu du ruban)
        - Les instructions basiques de la Machine de Turing del Vigna :
            * E0() : écriture d'un 0
            * E1() : écriture d'un 1
            * D() : déplacement à droite
            * G() : déplacement à gauche
        """
        entete = [
            "import sys",
            "sys.setrecursionlimit(3000)",
            "def init_ruban(taille1, taille2=0):     # taille1 et taille2 représentent les tailles des deux séquences de 1",
            "   # retourne un préfixe de 600 zéros (zones vides au début de la bande), une séquence de size1 1, un séparateur de deux 0, une deuxième séquence de size2 1 (si elle est utilisée), remplit le reste du ruban jusqu'à une longueur totale de 1200 (la longueur du ruban)",
            "   return ([0] * 600) + ([1] * taille1) + ([0] * 2) + ([1] * taille2) + ([0] * (1200 - taille1 - taille2 - 2 - 600))",
            "",
            "def E0() :",
            "    ruban[X] = 0  # Écriture d'un 0 à la position courante",
            "",
            "def E1() :",
            "    ruban[X] = 1  # Écriture d'un 1 à la position courante",
            "",
            "def D() :",
            "    global X",
            "    X += 1 # Déplacement de la tête vers la droite",
            "",
            "def G() :",
            "    global X",
            "    X -= 1 # Déplacement de la tête vers la gauche",
            "",
            "# Fonctions récursives pour les opérations sur listes",
            "def new_len(liste) :  # Calcule la longueur d'une liste de manière récursive",
            "   # Si la liste est vide (if not liste), retourne 0",
            "   # Sinon, retourne 1 (pour l'élément courant) + la longueur du reste de la liste (new_len(liste[1:]))",
            "   if not liste :",
            "       return 0",
            "   return 1 + new_len(liste[1:])",
            "",
            "def new_join(liste, index=0, resultat=\"\"):   # Construit une chaîne de caractères représentant les éléments d'une liste, de manière récursive",
            "   # liste : La liste à convertir en chaîne",
            "   # index : Position actuelle dans la liste (initialement 0)",
            "   # resultat : Chaîne accumulée au cours de la récursion",
            "   # Si l'index atteint la longueur de la liste (new_len(liste)), retourne la chaîne construite",
            "   if index == new_len(liste) :",
            "       return resultat",
            "   return new_join(liste, index + 1, resultat + \"{}\".format(liste[index]))",
            "",
            "ruban = [0] * 1200",
            "X = new_len(ruban) // 2",
            "",
        ]
        self.code.extend(entete)

    def generer_corps(self, nom_fichier) :
        """
        Gère l'initialisation du ruban selon les arguments qu'on veut que le script généré tienne compte (arguments qui dépendent quant à eux, de la tâche à effecuter choisie) :
        - Aucun argument : définit juste le nombre d'étapes par défaut (le ruban initialisé n'est donc composé que de 0 (1200))
        - Un argument ARG2 : initialise une plage d'une valeur de ARG2+1 cases à 1
        - Deux arguments ARG2 et ARG3 : initialise deux plages séparées par 2 cases, de ARG3+1 et ARG2+1 cases à 1
        """

        # argv[0] -> ARG0 : traducteur_q2.py
        # argv[1] -> ARG1 : ts_scripts/nom_du_script_TS_a_tester.TS
        # argv[2] -> ARG2 : un chiffre ou nombre s'il existe (c'est-à-dire s'il est fourni)
        # argv[3] -> ARG3 : un chiffre ou nombre s'il existe (c'est-à-dire s'il est fourni)
        # len(sys.argv) -> ARGC

        if len(sys.argv) == 2 :
            # Définit le nombre d'étapes par défaut si aucun argument qu'on veut que le script généré tienne compte
            self.ajouter_ligne("nb_etapes = 21")
        elif len(sys.argv) == 3 :
            # Initialise le ruban avec des 1 sur une plage de taille x
            m = sys.argv[2]
            self.ajouter_ligne("# Initialisation de la première plage de 1")
            self.ajouter_ligne("for i in range({}+1) :".format(m))
            self.ajouter_ligne("  ruban[X+i] = 1")
        elif len(sys.argv) == 4 :
            # Initialise deux plages successives de 1 sur le ruban, respectivement de taille m et n et séparées par 2 cases
            m = sys.argv[2]
            n = sys.argv[3]
            self.ajouter_ligne("# Initialisation de la première plage de 1")
            self.ajouter_ligne("for i in range({}+1) :".format(m))
            self.ajouter_ligne("    ruban[X+i] = 1")
            self.ajouter_ligne("# Initialisation de la seconde plage de 1 (séparée par 2 cases)")
            self.ajouter_ligne("for i in range({}+1) :".format(n))
            self.ajouter_ligne("    ruban[X+{}+3+i] = 1".format(m))

    def traduire_lignes(self, lignes) :
        """
        Traduit chaque ligne de code MTdV en instructions Python.
        Gère les commandes de base (G,D,0,1), l'affichage (I),les pauses (P), et les structures de contrôle (boucle, si).
        """
        for ligne in lignes :
            # On ne prend pas en compte les commentaires inline
            index = ligne.find("%")
            ligne = ligne[:index].strip() if index != -1 else ligne.strip()
            
            # Ajout d'espaces avant parenthèses et accolades ouvrantes et fermantes
            ligne = ligne.replace("(", " (")            
            ligne = ligne.replace("}", " }")

            # Découpage de la ligne en tokens
            tokens = ligne.split()
            i = 0
            while i < len(tokens) :
                if tokens[i] == "D" :
                    # Se déplace à droite
                    self.ajouter_ligne("D()")
                    
                elif tokens[i] == "G" :
                    # Se déplace à gauche
                    self.ajouter_ligne("G()")

                elif tokens[i] == "1" :
                    # Écrit 1 sur le ruban
                    self.ajouter_ligne("E1()")

                elif tokens[i] == "0" :
                    # Écrit 0 sur le ruban 
                    # (la MTdV ne peut que mettre des batons ou en enlever : écrire 0 revient à enlever le baton)
                    self.ajouter_ligne("E0()")
                    
                elif tokens[i] == "P":
                    # Met le programme en pause selon la valeur de nb_etapes
                    self.ajouter_ligne("global nb_etapes")
                    self.ajouter_ligne("if nb_etapes > 0 : ")
                    self.ajouter_ligne("     input('Appuyez sur la touche Entrée pour continuer')")
                    self.ajouter_ligne("     nb_etapes -= 1")
                    self.ajouter_ligne("     boucle0()")
                    self.ajouter_ligne("else :")
                    self.ajouter_ligne("     sys.exit()")

                elif tokens[i] == "I" :
                    # Commande d'affichage du ruban
                    # Affiche une fenêtre de 100 cases autour de la position courante
                    # (la position courante étant au centre de la fenêtre)
                    self.ajouter_ligne("")
                    self.ajouter_ligne("# Extraction de la fenêtre visible du ruban")
                    self.ajouter_ligne("ruban_visible = new_join(ruban[600-50:600+50])")
                    self.ajouter_ligne("print(ruban_visible) # Affichage du contenu")
                    self.ajouter_ligne("# Création de la ligne de marqueur de position")
                    self.ajouter_ligne("ligne_marqueur_pos = [' '] * 200")
                    self.ajouter_ligne("ligne_marqueur_pos[X-600+50] = 'X'")
                    self.ajouter_ligne("ligne_marqueur_pos = new_join(ligne_marqueur_pos)")
                    self.ajouter_ligne("print(ligne_marqueur_pos) # Affichage de la position")
                    self.ajouter_ligne("")

                elif tokens[i] == "boucle" :
                    # Début d'un bloc de boucle
                    self.boucle_nom_pos_ind.append((self.boucle_valeur_max, self.indentation_courante))
                    self.ajouter_ligne("def boucle{}():".format(self.boucle_nom_pos_ind[-1][0]))
                    self.indentation_courante += 1
                    self.boucle_valeur_max += 1
                    self.boucle_position_courante += 1

                elif tokens[i] == "si" :
                    # Début d'une condition
                    self.if_compteur += 1
                    i += 1
                    if tokens[i] == "(0)":
                        self.ajouter_ligne("if ruban[X] == 0 :")  # Test si la position courante contient un 0
                        self.indentation_courante += 1  
                    elif tokens[i] == "(1)" :
                        self.ajouter_ligne("if ruban[X] == 1 :")  # Test si la position courante contient un 1
                        self.indentation_courante += 1

                elif tokens[i] == "fin" :
                    # Fin de la boucle
                    if self.boucle_position_courante > 0:
                        self.ajouter_ligne("return")
                        self.indentation_courante -= 1
                        self.else_compteur += 1
                        self.ajouter_ligne("else :")
                        self.indentation_courante += 1

                elif tokens[i] == "}":
                    # Clôture d'un bloc condition ou boucle
                    if self.if_compteur > 0:
                        self.if_compteur -= 1
                        if self.boucle_position_courante == 0:
                            self.ajouter_ligne("sys.exit()")
                            self.indentation_courante -= 1

                    elif self.boucle_position_courante > 0:
                        # Appel récursif de la boucle
                        self.ajouter_ligne("boucle{}()".format(self.boucle_nom_pos_ind[-1][0]))
                        self.else_compteur -= 1
                        self.indentation_courante -= 1
                        
                        self.indentation_courante = self.boucle_nom_pos_ind[-1][-1]
                        self.ajouter_ligne("boucle{}()".format(self.boucle_nom_pos_ind[-1][0]))
                        self.boucle_nom_pos_ind.pop()
                        self.boucle_position_courante -= 1
                        
                i += 1

    def traduire_fichier(self, nom_fichier) :
        """
        Traduit le script TS en Python.
        Lit le fichier, filtre toutes les lignes et crée le script Python.
        """
        with open(nom_fichier, "r", encoding="latin-1") as fichier :
            contenu = fichier.read()
        lignes = []
        # Gestion des lignes vides et des commentaires
        for ligne in contenu.split("\n") :
            ligne = ligne.strip()
            if not ligne or ligne.startswith("%") or ligne == "#" :
                continue
            lignes.append(ligne)
        # Génère l'en-tête, le corps, et ensuite traduit le contenu
        self.generer_entete()
        self.generer_corps(nom_fichier)
        self.traduire_lignes(lignes)
        return "\n".join(self.code)

if __name__ == "__main__" :
    traducteur_q2 = MTdV_Traducteur_q2()
    translated_code = traducteur_q2.traduire_fichier(sys.argv[1])

    # Afficher le code traduit
    #print(translated_code)

    # Sauvegarder dans un fichier de sortie
    output_fichier = sys.argv[1].replace("ts_scripts", "py_scripts") .replace(".TS", "_Q2translated.py")
    with open(output_fichier, "w") as fichier :
        fichier.write(translated_code)
    print(f"Script Python généré : {output_fichier}")