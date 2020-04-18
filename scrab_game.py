#personal implementation of scrabble type game
#started 4/17/2020

from scrab_func import print_board, print_scores, get_letters
import random

#initialize lists
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]
tiles = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1, 2]
#initialize the board
scrab_grid = ["["+str(i).zfill(3)+"]" for i in range(225)]
#initialize player pieces
p1_pieces = []
p2_pieces = []

#initialize dictionaries
scrab_dict = {key:value for key, value in zip(letters, points)}
scrab_tiles = {key:value for key, value in zip(letters, tiles)}
player_points = {"Player 1":0, "Player 2":0}

#initialize the list of all tiles, for use to pull pieces to the player sets
all_pieces = []
def get_total(dict):
    total = 0
    for i in dict.values():
        total += i
    return total
num_pieces = get_total(scrab_tiles)
while num_pieces > 0:
    let = random.choice(letters)
    if scrab_tiles[let] > 0:
        scrab_tiles[let] -= 1
        all_pieces.append(let)
    num_pieces = get_total(scrab_tiles)
    

#game
print("Welcome to Scrabble!")
#print_board(scrab_grid)
#print_scores(player_points)

#initialize starting player pieces
get_letters(p1_pieces, all_pieces)
print(p1_pieces)
get_letters(p2_pieces, all_pieces)
print(p2_pieces)

