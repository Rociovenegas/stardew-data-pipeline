import xml.etree.ElementTree as ET
from pathlib import Path
import os

class ExperiencePoints:
    def __init__(self, node):
        self.points = []
        
        if node is not None:
            for child in node.findall("int"):
                if child.text is not None:
                    self.points.append(int(child.text))

    def __repr__(self):
        return f"ExperiencePoints({self.points})"

class Player:
    def __init__(self, player_node):
        self.name = self._get_text(player_node, "name")
        self.farm_name = self._get_text(player_node, "farmName")
        self.favorite_thing = self._get_text(player_node, "favoriteThing")

        exp_node = player_node.find("experiencePoints")
        self.experience_points = ExperiencePoints(exp_node)


    def _get_text(self, node, tag):
        
        element = node.find(tag)
        return element.text if element is not None else None

    def __repr__(self):
        return (
            f"Playername = {self.name}\n"
            f"farm_name = {self.farm_name}\n"
            f"favorite_thing = {self.favorite_thing}"
            # f"experience_points={self.experience_points})"
        )

# Testing...
# Upload the XML

if __name__ == '__main__':
    user_home = Path.home()
    path = user_home / "StardewValleyDashboard" / "Saves" / "test_430986684" / "test_430986684_20260219_161921_193927"
    tree = ET.parse(path)
    root = tree.getroot()
    player_node = root.find("player")
    print(player_node)
    player = Player(player_node)
    print(player)





