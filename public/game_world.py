
from public.player import Player
from public.enemy import Enemy
from public.weapon import Weapon

class GameWorld:
    def __init__(self):
        self.player = None
        self.enemies = []
        self.weapons = []

    def setup(self):
        # Create player
        self.player = Player(name="Hero")

        # Create enemies
        self.enemies.append(Enemy(type="Orc"))
        self.enemies.append(Enemy(type="Goblin"))

        # Create weapons
        self.weapons.append(Weapon(name="Sword", damage=20))
        self.weapons.append(Weapon(name="Bow", damage=15))

    def start_game(self):
        print("Game starts!")
        for enemy in self.enemies:
            print(f"An {enemy.type} appears!")
            self.weapons[0].use(enemy)  # Player uses the first weapon
            if enemy.health > 0:
                enemy.attack(self.player)
