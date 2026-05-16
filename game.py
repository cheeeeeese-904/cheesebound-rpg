"""Main Game class for Cheesebound RPG"""
import json
import os
from character import Player
from world import World
from combat import Combat
from save import SaveSystem

class Game:
    def __init__(self):
        self.player = None
        self.world = World()
        self.save_system = SaveSystem()

    def start(self):
        print("Welcome to Cheesebound!")
        if self.save_system.save_exists():
            if input("Load saved game? (y/n): ").lower() == 'y':
                self.player = self.save_system.load_game()
                if self.player:
                    self.game_loop()
                    return

        self.create_character()
        self.game_loop()

    def create_character(self):
        name = input("\nWhat is your name, adventurer? ")
        print("\nChoose your class:")
        print("1. Warrior (Strong, tanky)")
        print("2. Mage (Powerful spells)")
        print("3. Psychic (Earthbound-style PSI powers)")
        print("4. Rogue (Sneaky & lucky)")

        choice = input("Enter number: ")
        classes = {"1": "Warrior", "2": "Mage", "3": "Psychic", "4": "Rogue"}
        player_class = classes.get(choice, "Psychic")

        self.player = Player(name, player_class)
        print(f"\n{name} the {player_class} has begun their journey!")

    def game_loop(self):
        while True:
            print("\n" + "="*50)
            print(f"Location: {self.world.current_location.name}")
            print(f"HP: {self.player.hp}/{self.player.max_hp} | Level: {self.player.level}")
            print("\nWhat do you want to do?")
            print("1. Explore")
            print("2. Check Status")
            print("3. Inventory")
            print("4. Save Game")
            print("5. Quit")

            choice = input("Choice: ")

            if choice == "1":
                self.world.explore(self.player)
            elif choice == "2":
                self.player.show_status()
            elif choice == "3":
                self.player.show_inventory()
            elif choice == "4":
                self.save_system.save_game(self.player)
            elif choice == "5":
                if input("Save before quitting? (y/n): ").lower() == 'y':
                    self.save_system.save_game(self.player)
                print("Thanks for playing Cheesebound!")
                break
