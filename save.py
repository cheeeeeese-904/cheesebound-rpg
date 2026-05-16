import json
import os

class SaveSystem:
    def __init__(self):
        self.save_file = "savegame.json"

    def save_exists(self):
        return os.path.exists(self.save_file)

    def save_game(self, player):
        data = {
            "name": player.name,
            "player_class": player.player_class,
            "level": player.level,
            "exp": player.exp,
            "exp_to_level": player.exp_to_level,
            "hp": player.hp,
            "max_hp": player.max_hp,
            "attack": player.attack,
            "defense": player.defense,
            "psi": player.psi,
            "gold": player.gold,
            "inventory": player.inventory
        }
        with open(self.save_file, "w") as f:
            json.dump(data, f)
        print("Game saved!")

    def load_game(self):
        try:
            with open(self.save_file, "r") as f:
                data = json.load(f)

            from character import Player
            player = Player(data["name"], data["player_class"])

            player.level = data["level"]
            player.exp = data["exp"]
            player.exp_to_level = data["exp_to_level"]
            player.hp = data["hp"]
            player.max_hp = data["max_hp"]
            player.attack = data["attack"]
            player.defense = data["defense"]
            player.psi = data["psi"]
            player.gold = data["gold"]
            player.inventory = data["inventory"]

            print("Game loaded successfully!")
            return player
        except:
            print("Failed to load save.")
            return None
