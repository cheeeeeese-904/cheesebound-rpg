import random

class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.level = 1
        self.exp = 0
        self.exp_to_level = 100

        self.max_hp = 50 if player_class == "Warrior" else 40
        self.hp = self.max_hp
        self.attack = 12 if player_class == "Warrior" else 8
        self.defense = 8 if player_class == "Warrior" else 5
        self.psi = 15 if player_class == "Psychic" else 8

        self.inventory = ["Wooden Sword", "Cheese Wheel", "Potion"]
        self.gold = 25

    def show_status(self):
        print(f"\n=== {self.name} the {self.player_class} ===")
        print(f"Level: {self.level} | EXP: {self.exp}/{self.exp_to_level}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Attack: {self.attack} | Defense: {self.defense} | PSI: {self.psi}")
        print(f"Gold: {self.gold}")

    def show_inventory(self):
        print("\n=== Inventory ===")
        for item in self.inventory:
            print(f"- {item}")
        print(f"Gold: {self.gold}")

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= self.exp_to_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp = 0
        self.exp_to_level = int(self.exp_to_level * 1.5)
        self.max_hp += 10
        self.hp = self.max_hp
        self.attack += 3
        self.defense += 2
        print(f"\n🎉 LEVEL UP! You are now level {self.level}!")
