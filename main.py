
from public import Player, Enemy, Weapon, GameWorld
from public.utils import delay_action

def main():
    # Initialize game world
    game = GameWorld()
    game.setup()

    # Start the game
    delay_action(2, "starting the game")
    game.start_game()

    print("Game over. Thank you for playing!")

if __name__ == "__main__":
    main()
