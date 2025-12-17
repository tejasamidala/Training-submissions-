import random


# ---------------- Encapsulation (data hiding) ----------------
class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role

        self.__hp = 0
        self.__max_hp = 0
        self.__attack = 0
        self.__defense = 0

        # Composition: Player HAS an Inventory (not inheritance)
        self.inventory = Inventory()

        self._set_stats_by_role()

    def _set_stats_by_role(self):
        role = self.role.lower()
        if role == "warrior":
            self.__max_hp = 120
            self.__attack = 16
            self.__defense = 6
        elif role == "mage":
            self.__max_hp = 90
            self.__attack = 22
            self.__defense = 3
        elif role == "rogue":
            self.__max_hp = 100
            self.__attack = 18
            self.__defense = 4
        else:
            # default fallback
            self.__max_hp = 100
            self.__attack = 15
            self.__defense = 4

        self.__hp = self.__max_hp

    # getters (controlled access)
    @property
    def hp(self):
        return self.__hp

    @property
    def max_hp(self):
        return self.__max_hp

    @property
    def attack(self):
        return self.__attack

    @property
    def defense(self):
        return self.__defense

    def is_alive(self):
        return self.__hp > 0

    def take_damage(self, dmg):
        self.__hp = max(0, self.__hp - dmg)

    def heal(self, amount):
        self.__hp = min(self.__max_hp, self.__hp + amount)

    def __str__(self):
        return f"{self.name} ({self.role}) HP: {self.hp}/{self.max_hp}"


class Enemy:
    def __init__(self, name, hp, attack, defense, gold_drop):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.gold_drop = gold_drop

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp = max(0, self.hp - dmg)

    def __str__(self):
        return f"{self.name} HP: {self.hp}"


# ---------------- Composition: Inventory & Items ----------------
class Item:
    def __init__(self, name, kind, value):
        self.name = name          # e.g. "Small Potion"
        self.kind = kind          # "heal" or "buff"
        self.value = value        # heal amount or buff amount

    def __str__(self):
        return f"{self.name} ({self.kind}: {self.value})"


class Inventory:
    def __init__(self):
        self.__items = []
        self.__gold = 0

    @property
    def gold(self):
        return self.__gold

    def add_gold(self, amount):
        self.__gold += amount

    def add_item(self, item):
        self.__items.append(item)

    def list_items(self):
        if not self.__items:
            print("Inventory is empty.")
            return
        for i, item in enumerate(self.__items, start=1):
            print(f"{i}. {item}")

    def use_item(self, index, player):
        if index < 1 or index > len(self.__items):
            print("Invalid item number.")
            return False

        item = self.__items.pop(index - 1)

        if item.kind == "heal":
            player.heal(item.value)
            print(f"Used {item.name}. Healed {item.value} HP.")
            return True

        print("That item can't be used right now.")
        return False


# ---------------- Combat System ----------------
def calc_damage(attacker_attack, defender_defense):
    base = attacker_attack - defender_defense
    variance = random.randint(-2, 3)
    dmg = max(1, base + variance)
    return dmg


def fight(player, enemy):
    print("\n--- Combat Start ---")
    print(player)
    print(enemy)

    while player.is_alive() and enemy.is_alive():
        print("\nChoose action:")
        print("1. Attack")
        print("2. Use potion")
        action = input("Enter 1 or 2: ").strip()

        if action == "1":
            dmg = calc_damage(player.attack, enemy.defense)
            enemy.take_damage(dmg)
            print(f"You hit {enemy.name} for {dmg} damage. Enemy HP: {enemy.hp}")

        elif action == "2":
            if player.inventory.gold < 0:  # never true, but kept simple
                pass
            print("Your items:")
            player.inventory.list_items()
            choice = input("Item number to use (or press Enter to cancel): ").strip()
            if choice == "":
                continue
            if choice.isdigit():
                player.inventory.use_item(int(choice), player)
                print(player)
            else:
                print("Invalid input.")

        else:
            print("Invalid action. Try again.")
            continue

        # Enemy turn (if alive)
        if enemy.is_alive():
            dmg = calc_damage(enemy.attack, player.defense)
            player.take_damage(dmg)
            print(f"{enemy.name} hits you for {dmg}. Your HP: {player.hp}/{player.max_hp}")

    print("--- Combat End ---")

    if player.is_alive():
        print(f"You defeated {enemy.name}!")
        player.inventory.add_gold(enemy.gold_drop)
        print(f"You gained {enemy.gold_drop} gold. Total gold: {player.inventory.gold}")
        return True

    print("You were defeated... Game over.")
    return False


# ---------------- Game Loop ----------------
def random_enemy():
    enemies = [
        Enemy("Goblin", hp=35, attack=10, defense=2, gold_drop=10),
        Enemy("Wolf", hp=40, attack=12, defense=3, gold_drop=12),
        Enemy("Bandit", hp=50, attack=14, defense=4, gold_drop=18),
    ]
    return random.choice(enemies)


def shop(player):
    print("\n--- Shop ---")
    print(f"Gold: {player.inventory.gold}")
    print("1. Small Potion (heal 25) - 10 gold")
    print("2. Medium Potion (heal 50) - 18 gold")
    print("3. Leave shop")
    choice = input("Choose 1-3: ").strip()

    if choice == "1":
        cost = 10
        if player.inventory.gold >= cost:
            player.inventory.add_gold(-cost)
            player.inventory.add_item(Item("Small Potion", "heal", 25))
            print("Bought Small Potion.")
        else:
            print("Not enough gold.")
    elif choice == "2":
        cost = 18
        if player.inventory.gold >= cost:
            player.inventory.add_gold(-cost)
            player.inventory.add_item(Item("Medium Potion", "heal", 50))
            print("Bought Medium Potion.")
        else:
            print("Not enough gold.")
    else:
        print("Leaving shop.")


def main():
    print("Text RPG (simple)")
    name = input("Enter your character name: ").strip() or "Player"

    print("Choose class: warrior / mage / rogue")
    role = input("Enter class: ").strip().lower()
    if role not in ["warrior", "mage", "rogue"]:
        role = "warrior"

    player = Player(name, role)
    player.inventory.add_gold(15)
    player.inventory.add_item(Item("Small Potion", "heal", 25))

    print("\nCreated character:")
    print(player)
    print(f"Starting gold: {player.inventory.gold}")

    while player.is_alive():
        print("\nMain Menu:")
        print("1. Fight enemy")
        print("2. Inventory")
        print("3. Shop")
        print("4. Quit")
        choice = input("Enter 1-4: ").strip()

        if choice == "1":
            enemy = random_enemy()
            won = fight(player, enemy)
            if not won:
                break

        elif choice == "2":
            print("\n--- Inventory ---")
            print(f"Gold: {player.inventory.gold}")
            player.inventory.list_items()

        elif choice == "3":
            shop(player)

        elif choice == "4":
            print("Bye.")
            break
        else:
            print("Invalid choice.")git

    print("\nDone.")


if __name__ == "__main__":
    main()
    elif action == "3":
    print("You ran away safely!")
    break
