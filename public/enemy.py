
class Enemy:
    def __init__(self, type: str, health: int = 50):
        self.type = type
        self.health = health

    def attack(self, player):
        damage = 10
        print(f"The {self.type} attacks {player.name} for {damage} damage!")
        player.take_damage(damage)

    def take_damage(self, amount: int):
        self.health -= amount
        print(f"The {self.type} takes {amount} damage. Health is now {self.health}.")
