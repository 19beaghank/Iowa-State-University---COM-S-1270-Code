#Kevin Beaghan 4/22/2025
#COMS 1270 1 -  This is a version of the classic boardgame 'Candy Land' - called 'Candy Realm!'

import random
from colorama import Fore, Style, init

# Pypi Colorama 0.4.6
# https://pypi.org/project/colorama/
# Accessed 4/30/2025

init()
colors = {'R': Fore.RED,
'Y': Fore.YELLOW,
'B': Fore.BLUE,
'P': Fore.MAGENTA,
'O': Fore.CYAN,
'G': Fore.GREEN}

class Player:
    def __init__(self, name, number, computer=False):
        self.name = name
        self.number = str(number)
        self.position = 0
        self.computer = computer

    def move_to_next(self, board, target):
        try:
            next_position = board.index(target, self.position + 1)
            self.position = next_position
        except ValueError:
            print(f"{self.name} can't find another '{target}', staying at position {self.position}.")
            return
        print(f"{self.name} moves to the next '{target}' at position {self.position}")

class Game:
    def __init__(self, computer_players):
        self.board = self.generate_board()
        self.players = self.create_players(computer_players)
        self.cards = ['R', 'Y', 'B', 'P', 'O', 'G']

    def generate_board(self):
        spaces = ['R', 'Y', 'B', 'P', 'O', 'G'] * 16
        for i in range(4):
            spaces += random.choice(['R', 'Y', 'B', 'P', 'O', 'G'])
        random.shuffle(spaces)
        return spaces

    def create_players(self, computer_players):
        players = []
        for i in range(computer_players):
            name = input(f"Enter name for Player {i+1}: ")
            players.append(Player(name, i + 1))
        for i in range(computer_players, 4):
            players.append(Player(f"Computer {i+1}", i + 1, computer=True))
        return players

    def draw(self):
        return random.choice(self.cards)

    def reshuffle(self):
        random.shuffle(self.cards)
        print("\nThe deck has been reshuffled")

    def display_board(self):
        board_display = [" " * (len(self.board) * 2)] * len(self.players)
        for p_idx, player in enumerate(self.players):
            row_display = list(" " * (len(self.board) * 2))
            row_display[player.position * 2] = player.number
            board_display[p_idx] = "".join(row_display)
        board_state = "\n".join(board_display)
        board_spaces = " ".join(colors[letter] + letter for letter in self.board)
        print("\nGame Board:")
        print(board_state)
        print(board_spaces + Style.RESET_ALL)

    def play_turn(self, player):
        print(f"\n{player.name}'s turn:")
        letter = self.draw()
        card = colors[letter] + letter + Style.RESET_ALL
        print(f"Next card: '{card}'")
        if not player.computer:
            reshuffle = input("Do you want to reshuffle the deck, [y]es or [n]o? ")
            if reshuffle == "y":
                self.reshuffle()
                return False
        player.move_to_next(self.board, letter)
        self.display_board()
        if player.position >= len(self.board) - 1:
            print(f"Congradulations! {player.name} wins!")
            return True
        return False

    def start_game(self):
        self.display_board()
        game_over = False
        while not game_over:
            for player in self.players:
                game_over = self.play_turn(player)
                if game_over:
                    break
        return self.rematch()

    def rematch(self):
        while True:
            choice = input("\nWould you like to play again, [y]es or [n]o? ")
            if choice == "y":
                return True
            elif choice == "n":
                print("Thank you for playing, goodbye")
                return False
            else:
                print("Please only enter y or n")

def main():
    while True:
        print("""Candy Realm!
By: Kevin Beaghan
[COM S 127 1]
-------------------------------------------------------\n""")
        menu = input("Would you like to [p]lay, read the [r]ules, or [q]uit: ")
        if menu == "p":
            while True:
                try:
                    computer_players = int(input("Enter number of human players (1-4): "))
                    if 1 <= computer_players <= 4:
                        break
                    else:
                        print("Please enter a number between 1 and 4.")
                except ValueError:
                    print("Please enter a number.")
            game = Game(computer_players)
            play_again = game.start_game()
            if not play_again:
                break
        elif menu == "r":
            print("""\nRules:
- The board consists of 100 randomly shuffled colored spaces of 'R', 'Y', 'B', 'P', 'O', and 'G'
- Players draw a card to determine where they move next
- The drawn card tells the player to move to the next occurrence of that letter
- The first player to land on the last space wins
- If unable to move, players can reshuffle the deck, passing their turn\n""")
        elif menu == "q":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter p, r, or q.\n")

if __name__ == "__main__":
    main()