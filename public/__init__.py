# /public/__init__.py

# Expose the key classes for easier imports
from .player import Player
from .enemy import Enemy
from .weapon import Weapon
from .game_world import GameWorld

# Version or metadata about the package
__version__ = "1.0.0"
__author__ = "Your Name"
__description__ = "Game Development Project using OOP principles"

# Optional initialization code
print("Game package loaded successfully.")
