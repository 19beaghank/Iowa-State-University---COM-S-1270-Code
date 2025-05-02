#Kevin Beaghan 2/24/2025
#Assignment 3 - Creating a game

import random

print("""NIMGRAB!
Kevin Beaghan
[COM S 127 1]
""")

def rematch():
    again = input("Would you like to [p]lay again or [q]uit?")
    if again == "p":
        main()
    elif again == "q":
        print("Thank you for playing")
    else:
        print("Please only enter [p]lay or [q]uit")
        rematch()

def validate_move(move):
    valid = True
    while valid:
        if 0>move or move>3:
            print("Please only enter an 1, 2, or 3")
            move = int(input("How many pieces will P1 take (1-3)?"))
        else:
            return move
            valid = False

def check_board(pieces, move):
    if pieces == 1:
        print(f"The number of pieces in play are: {pieces}")
        print("| "*pieces)
        print("Game over: You win!")
        rematch()
    validate = True
    while validate:
        if pieces<1:
            print("Invalid move: cannot take more pieces than are present")
            pieces = pieces+move
            move = int(input("How many pieces will you take (1-3)?"))
            validate_move(move)
            pieces = pieces-move
        else:
            return pieces
            try_again=False

def check_board1(pieces, move):
    if pieces == 1:
        print(f"The number of pieces in play are: {pieces}")
        print("| "*pieces)
        print("Game over: You win!")
        rematch()
    validate = True
    while validate:
        if pieces<1:
            print("Invalid move: cannot take more pieces than are present")
            pieces = pieces+move
            move = int(input("How many pieces will P1 take (1-3)?"))
            validate_move(move)
            pieces = pieces-move
        else:
            return pieces
            try_again=False

def check_board2(pieces, move):
    if pieces == 1:
        print(f"The number of pieces in play are: {pieces}")
        print("| "*pieces)
        print("Game over: You win!")
        rematch()
    validate = True
    while validate:
        if pieces<1:
            print("Invalid move: cannot take more pieces than are present")
            pieces = pieces+move
            move = int(input("How many pieces will P2 take (1-3)?"))
            validate_move(move)
            pieces = pieces-move
        else:
            return pieces
            try_again=False

def P2_first(pieces):
    while pieces >=1:          
        print(f"The number of pieces in play are: {pieces}")
        print("| "*pieces)
        move = int(input("How many pieces will P2 take (1-3)?"))
        validate_move(move)
        pieces = pieces-move
        check_board2(pieces, move)
        print(f"The number of pieces in play are: {pieces}")
        print("| "*pieces)
        move = int(input("How many pieces will P1 take (1-3)?"))
        validate_move(move)
        pieces = pieces-move
        check_board1(pieces, move)

def P1_first(pieces):
    while pieces >1:          
        print(f"The number of pieces in play are: {pieces}")
        print("| "*pieces)
        move = int(input("How many pieces will P1 take (1-3)?"))
        validate_move(move)
        pieces = pieces-move
        check_board1(pieces, move)
        print(f"The number of pieces in play are: {pieces}")
        print("| "*pieces)
        move = int(input("How many pieces will P2 take (1-3)?"))
        validate_move(move)
        pieces = pieces-move
        check_board2(pieces, move)

def computer_game(pieces):
    while pieces >1:          
            print(f"The number of pieces in play are: {pieces}")
            print("| "*pieces)
            move = int(input("How many pieces will you take (1-3)?"))
            validate_move(move)
            pieces = pieces-move
            check_board(pieces, move)
            print(f"The number of pieces in play are: {pieces}")
            print("| "*pieces)
            if pieces>4:
                move = random.randrange(1,4)
                print(f"The computer takes {move} piece(s)")
                pieces=pieces-move
            elif pieces ==4:
                move = 3
                print(f"The computer takes {move} piece(s)")
                pieces = pieces-move
                print(f"The number of pieces in play are: {pieces}")
                print("| "*pieces)
                print("Game over: You lose")
                rematch()
            elif pieces ==3:
                move = 2
                pieces = pieces-move
                print(f"The number of pieces in play are: {pieces}")
                print("| "*pieces)
                print("Game over: You lose")
                rematch()
            elif pieces==2:
                move = 1
                print(f"The computer takes {move} piece(s)")
                print(f"The number of pieces in play are: {pieces}")
                print("| "*pieces)
                print("Game over: You lose")
                rematch()
            elif pieces==1:
                print("Game over: You win")
                rematch()

def players():
    pieces = random.randrange(20,25)
    play = input("Would you like to play [s]olo or with a [f]riend?")
    if play == "s":
        computer_game(pieces)
    elif play == "f":
        player = input("Who would like to go first, [P1] or [P2]?")
        if player == "P1":
            P1_first(pieces)
        elif player == "P2":
            P2_first(pieces)
        else:
            print("Please only select [P1] or [P2]")
            players()
    else:
        players()

def main():
    menu = input("Would you like to [p]lay, see the [r]ules, or [e]xit?")
    if menu == "p":
        players()
    elif menu == "r":
        print("""Players alternate turns removing items from play
        When it is their turn, a player takes 1, 2, or 3 items from play
        Players cannot take more items than are currently in play
        The game starts with the player when in 1-player mode, and with whoever you decide
        to go first in 2-player mode

        WIN CONDITION:
        The player who takes the last item loses. 
        """)
        main()
    elif menu == "e":
        print("Goodbye")
    else:
        main()

if __name__ == "__main__":
    main()