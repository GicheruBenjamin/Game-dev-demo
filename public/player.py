
class Player:
    def __init__(self, name: str, health: int = 100):
        self.name = name
        self.health = health
        self.score = 0

    def take_damage(self, amount: int):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Health is now {self.health}.")

    def add_score(self, points: int):
        self.score += points
        print(f"{self.name}'s score increased by {points}. Total score: {self.score}")
