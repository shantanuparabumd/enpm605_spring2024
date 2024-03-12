import sys
import os.path
<<<<<<< HEAD
folder = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(folder)
# Import your functions

from rpg.item import Item  # noqa: E402
=======
path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path)
# Import your functions

>>>>>>> c1e13759811ca5dc703ed81338a61b5958563aeb
from rpg.player import Player  # noqa: E402
from rpg.enemy import Enemy  # noqa: E402
import random  # noqa: E402
# from lecture6.rpg.enemy import Enemy
# from lecture6.rpg.maze import Maze
# from lecture6.rpg.item import Item

if __name__ == "__main__":
    # Create a player
    
    player = Player("Link", 150)
    enemy = Enemy("Ganon")
<<<<<<< HEAD
    # game_action = [player.attack, enemy.attack]
    
    # while player.health > 0:
    #     action = random.choice(game_action)
    #     if action == player.attack:
    #         action(enemy, 20)
    #     elif action == enemy.attack:
    #         action(player, 30)
    #     else:
    #         print("Invalid action")
    
    
    print(player)
    # Pick up arrow
    player.pick_up(Item("Arrow", "Long range attack", "arrow"))
    # Pick up key
    player.pick_up(Item("Key", "A golden key", "key"))
    # Pick up heart
    player.pick_up(Item("Heart", "A heart container", "heart"))
    print(player)
    
    player.use_item("arrow")
    print(player)
    player.use_item("arrow")
    print(player)
=======
    game_action = [player.attack, enemy.attack]
    
    while player.health > 0:
        action = random.choice(game_action)
        if action == player.attack:
            action(enemy, 20)
        elif action == enemy.attack:
            action(player, 30)
        else:
            print("Invalid action")
>>>>>>> c1e13759811ca5dc703ed81338a61b5958563aeb
