import random
from combat import battle, Enemy

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class World:
    def __init__(self):
        self.current_location = Location("Cheese Village", "A peaceful village famous for its legendary cheese.")
        self.locations = {
            "village": self.current_location,
            "forest": Location("Mysterious Forest", "Trees whisper bad jokes here..."),
            "dungeon": Location("Abandoned Cheese Dungeon", "It smells weirdly good in here."),
        }

    def explore(self, player):
        print(f"\n{self.current_location.description}")
        print("\nYou wander around...")

        if random.random() < 0.6:
            enemy = random.choice([
                Enemy("Goblin with a Bad Attitude", 25, 8, 3, 20),
                Enemy("Possessed Cheese Elemental", 40, 12, 5, 35),
                Enemy("Tax Collector Imp", 30, 10, 4, 25),
            ])
            battle(player, enemy)
        else:
            event = random.choice([
                "You found a shiny rock! (+5 gold)",
                "A friendly squirrel gives you a Potion!",
                "You step in something sticky... but find 15 gold!"
            ])
            print(event)
            if "gold" in event.lower():
                player.gold += 15
            elif "potion" in event.lower():
                player.inventory.append("Potion")

        # Chance to change location
        if random.random() < 0.4:
            new_loc = random.choice(list(self.locations.values()))
            self.current_location = new_loc
            print(f"\nYou travel to {new_loc.name}!")
