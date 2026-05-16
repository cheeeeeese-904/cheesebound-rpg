"""Cheesebound RPG - Main Entry Point"""
from game import Game

def main():
    print("\n=== CHEESEBOUND RPG ===")
    print("Earthbound vibes in a fantasy world!\n")
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
