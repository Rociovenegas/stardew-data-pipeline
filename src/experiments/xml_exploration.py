import xml.etree.ElementTree as ET
from pathlib import Path


def print_tree(node, path=None):
    if path is None:
        path = []

    # Agregamos el nodo actual al camino
    current_path = path + [node.tag]

    # Imprimimos la ruta completa
    print(" -> ".join(current_path))

    # Recorremos los hijos
    for child in node:
        print_tree(child, current_path)


# Cargar el XML
tree = ET.parse("/Users/rocio/StardewValleyDashboard/Saves/test_430986684/test_430986684_20260219_161921_193927")
root = tree.getroot()

# Nodo raíz
print(f"root:{root}")
print(f"nombre del nodo raíz: {root.tag}")     
print(f"atributos del nodo raíz (si los tiene): {root.attrib}") 


#SaveGame -> player 
player = root.find('player')

#SaveGame -> player -> name -> test_mizu
name_player = player.find('name').text

# SaveGame -> player -> experiencePoints -> int
experience_points = player.find('experiencePoints')
experience_points_int = experience_points.findall('int')


# SaveGame -> player -> <favoriteThing>gatos</favoriteThing>
favorite_thing = player.find('favoriteThing').text

# teoricamente se puede calcular con experience level
farming_level = player.find('farmingLevel').text
mining_level = player.find('miningLevel').text
combat_level = player.find('combatLevel').text
foraging_level = player.find('foragingLevel').text
fishing_level = player.find('fishingLevel').text

#SaveGame -> player -> totalMoneyEarned>
total_money_earned = player.find('totalMoneyEarned')

#SaveGame -> player -> money
money = player.find('money')

# SaveGame -> currentSeason
season = root.find('currentSeason').text

# SaveGame ->	<dayOfMonth>1</dayOfMonth>
day = root.find('dayOfMonth').text

# SaveGame ->	<year>1</year>
year = root.find('year').text 

# --- PRINT DE RESULTADOS ---
print("\n--- Información del jugador ---")
print(f"Nombre: {name_player}")
print(f"Cosa favorita: {favorite_thing}")
for exp in experience_points_int:
    print(f"exp: {exp.text}")
print(f"foraging level: {foraging_level} ")
print(f"Dinero total ganado: {total_money_earned}")
print(total_money_earned.text.strip())
print(f"Dinero en bolsillo: {money}")
print(money.text.strip())

print(f"Fecha: Año {year}, Día {day}, Temporada {season}")
if total_money_earned is not None:
    print("Texto crudo:", repr(total_money_earned.text))



# print_tree(root)

# for child in player:
#     print(child.tag)

# money = player.find('money')
# print("Resultado find:", money)

