import os
import random


# TODO: 
# check if a block used cann't draw on it
# decide winner


board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
def set_to_board(x, y, hand):
    global board
    if x < 3 and y < 3:
        if hand == "user":
            board[x][y] = "O"
        else:
            board[x][y] = "X"

def draw_board():
    os.system("clear")
    for line in board:
        line_str = f"{'-'*13}\n| {line[0]} | { line[1]} | {line[2]} |"
        print(line_str)
    print('-'*13)

def decide_winner():
    pass

def computer_hand():
    x = random.randrange(3)
    y = random.randrange(3)
    set_to_board(x, y, "computer")



def main():
    for _ in range(3):
        draw_board()
        x = int(input("x :> "))
        y = int(input("y :> "))
        set_to_board(x, y, "user")
        computer_hand()
    draw_board()


if __name__ == "__main__":
    main()
