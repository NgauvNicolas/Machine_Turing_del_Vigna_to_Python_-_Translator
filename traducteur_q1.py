import json
import sys

# Initialisation des variables globales
ruban = []  # Le ruban, représenté comme une liste
io_head_index = 0  # Position de la tête de lecture-écriture

# Dictionnaire des fonctions correspondant aux instructions MdTV
def start():
    # Rien à faire pour l'instruction "start"
    pass

def move_right():
    global io_head_index
    io_head_index += 1
    if io_head_index >= len(ruban):
        ruban.append('0')  # Étend le ruban si nécessaire

def move_left():
    global io_head_index
    if io_head_index > 0:
        io_head_index -= 1
    else:
        raise IndexError("La tête ne peut pas dépasser le bord gauche du ruban.")

def write_0():
    global ruban, io_head_index
    ruban[io_head_index] = '0'

def write_1():
    global ruban, io_head_index
    ruban[io_head_index] = '1'

def if_read_0(next_nodes):
    global ruban, io_head_index
    return next_nodes[0] if ruban[io_head_index] == '0' else next_nodes[1]

def if_read_1(next_nodes):
    global ruban, io_head_index
    return next_nodes[0] if ruban[io_head_index] == '1' else next_nodes[1]

def print_machine_state():
    global ruban, io_head_index
    print("Ruban:", ''.join(ruban))
    print("Position:", ' ' * io_head_index + 'X')

def loop(body_nodes):
    while True:
        for node_id in body_nodes:
            if execute_node(node_id):
                return

def end():
    # Rien à faire pour "end"
    pass

# Map des instructions aux fonctions correspondantes
instruction_map = {
    "start": start,
    "move right": move_right,
    "move left": move_left,
    "write 0": write_0,
    "write 1": write_1,
    "if read 0": if_read_0,
    "if read 1": if_read_1,
    "print machine state": print_machine_state,
    "loop": loop,
    "end": end
}

# Fonction pour exécuter un nœud
nodes = []  # Les nœuds du programme chargé

def execute_node(node_id):
    global nodes
    node = nodes[node_id]

    instruction = node["inst"]
    edges = node.get("edges", [])
    body = node.get("body", [])

    if instruction in ["if read 0", "if read 1"]:
        return instruction_map[instruction]([edge[0] for edge in edges])
    elif instruction == "loop":
        instruction_map[instruction]([edge[0] for edge in edges if edge[1] == "start loop"])
    else:
        instruction_map[instruction]()

    # Suivant logique par défaut
    return edges[0][0] if edges else None

# Chargement et exécution du programme MdTV
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python traducteur.py <fichier_json>")
        sys.exit(1)

    fichier_json = sys.argv[1]

    try:
        with open(fichier_json, 'r') as f:
            programme = json.load(f)
    except Exception as e:
        print("Erreur lors du chargement du fichier JSON:", e)
        sys.exit(1)

    # Initialisation des nœuds et du ruban
    nodes = programme["nodes"]
    ruban = ['0'] * 100  # Initialisation avec un ruban par défaut de 100 cellules
    io_head_index = 50   # Position initiale au centre du ruban

    # Exécution du programme MdTV
    current_node_id = 0
    while current_node_id is not None:
        current_node_id = execute_node(current_node_id)
