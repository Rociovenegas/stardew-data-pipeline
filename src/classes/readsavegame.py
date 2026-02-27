from pathlib import Path
from src.parsers.generate_fields import find_node_by_path, generate_from_save_file, save_as_python_dict

class ReadSaveGame:
    def __init__(self, save_path, element=None):
        self.save_path = save_path
        self.element = element
        self.node = None
        self.fields = None
    
    def load(self):
        self.node = find_node_by_path(self.save_path, self.element)
        if self.node is not None:
            self.fields = generate_from_save_file(self.node)
        return self.fields
    
    def save_fields(self, output_file="savegame_fields.txt"):
        if self.fields:
            save_as_python_dict(self.fields, output_file)
            print(f"Total fields found: {len(self.fields)}\n")

save_path=Path.home() / "StardewValleyDashboard" / "Saves" / "test_430986684" / "test_430986684_20260219_161921_193927"
saveGame = ReadSaveGame(save_path=save_path)
savegame_fields = saveGame.load()

if savegame_fields:
    saveGame.save_fields(output_file="savegame_fields.txt")

player = ReadSaveGame(save_path=save_path, element="player")
player_fields = player.load()
if player_fields:
    player.save_fields(output_file="player_fields.txt")
