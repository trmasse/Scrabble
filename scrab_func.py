#functions for Scrabble game
import random

def print_board(grid):
    i = 0
    while i < len(grid):
        print(" ".join(grid[i:i+15]))
        i += 15
    
def print_scores(scores):
    print("Player 1 has {} points.".format(scores["Player 1"]))
    print("Player 2 has {} points.".format(scores["Player 2"]))
    
def get_letters(player, letters):
    if len(letters) > 0:
        if len(letters) < 7-len(player):
            while len(letters) > 0:
                let = random.choice(letters)
                letters.remove(let)
                player.append(let)
        else:
            while len(player) < 7:
                let = random.choice(letters)
                letters.remove(let)
                player.append(let)