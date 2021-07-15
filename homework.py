# I am the game of tic tac toe
def init():
    available_spots = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

def print_board(available_spots):
    print(f"\t{available_spots[0]} | {available_spots[1]} | {available_spots[2]}")
    print(f"\t---------------")
    print(f"\t{available_spots[3]} | {available_spots[4]} | {available_spots[5]}")
    print(f"\t---------------")
    print(f"\t{available_spots[6]} | {available_spots[7]} | {available_spots[8]}")

def player_turn(player):
    print("It is player {player}'s turn")
    print("Select a position to play")
    position = input("> ")
    if player = "X":
        available_spots[position] = "X"
    if player = "O":
        available_spots[position] = "O"

def check_win_state():
    


def main():
    init()
    for i i
    print_board()
