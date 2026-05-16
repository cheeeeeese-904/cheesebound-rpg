import random

class Enemy:
    def __init__(self, name, hp, attack, defense, exp_reward):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.exp_reward = exp_reward

enemies = [
    Enemy("Goblin with a Bad Attitude", 25, 8, 3, 20),
    Enemy("Possessed Cheese Elemental", 40, 12, 5, 35),
    Enemy("Tax Collector Imp", 30, 10, 4, 25),
    Enemy("Angry Scarecrow", 35, 9, 6, 30),
]

def battle(player, enemy):
    print(f"\nA wild {enemy.name} appears!")

    while player.hp > 0 and enemy.hp > 0:
        print(f"\nYour HP: {player.hp} | {enemy.name}'s HP: {enemy.hp}")

        print("\n1. Attack  2. Special  3. Item  4. Run")
        choice = input("Choose action: ")

        if choice == "1":
            dmg = max(1, player.attack - enemy.defense + random.randint(-2, 3))
            enemy.hp -= dmg
            print(f"You hit the {enemy.name} for {dmg} damage!")
        elif choice == "2":
            if player.player_class == "Psychic":
                dmg = player.psi + random.randint(5, 15)
                enemy.hp -= dmg
                print(f"You use PSI ROCKIN'! {dmg} psychic damage!")
            else:
                dmg = player.attack + 5
                enemy.hp -= dmg
                print(f"You use your special attack for {dmg} damage!")
        elif choice == "3":
            if "Potion" in player.inventory:
                player.hp = min(player.max_hp, player.hp + 25)
                player.inventory.remove("Potion")
                print("You drink a Potion and recover HP!")
            else:
                print("No potions left!")
                continue
        elif choice == "4":
            if random.random() < 0.6:
                print("You escaped!")
                return
            else:
                print("Couldn't escape!")

        # Enemy attack
        if enemy.hp > 0:
            dmg = max(1, enemy.attack - player.defense + random.randint(-2, 2))
            player.hp -= dmg
            print(f"The {enemy.name} hits you for {dmg} damage!")

    if player.hp > 0:
        print(f"\nYou defeated the {enemy.name}!")
        player.gain_exp(enemy.exp_reward)
        player.gold += random.randint(10, 25)
    else:
        print("\nYou were defeated... Game Over.")
        exit()
