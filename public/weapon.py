class Weapon:
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage

    def use(self, enemy):
        print(f"Weapon {self.name} used! Deals {self.damage} damage to {enemy.type}.")
        enemy.take_damage(self.damage)
