# Kevin Beaghan 4/6/2025
# [COMS 1270 A] Week 12 Lab - Using unit tests to create a game of rock paper scissors against the computer

import random

def playRound(human):
    computer = generateComputerMove()
    print(f"Computer chose: {computer}")
    winner = determineWinner(human, computer)
    if winner == "Draw":
        return "It's a draw!"
    elif winner == human:
        return "Human Wins!"
    else:
        return "Computer Wins!"

def determineWinner(human, computer):
    if human == computer:
        return "Draw"
    elif (human == "Rock" and computer == "Scissors") or (human == "Paper" and computer == "Rock") or (human == "Scissors" and computer == "Paper"):
        return human
    else:
        return computer

def generateComputerMove():
    return random.choice(["Rock", "Paper", "Scissors"])

def main():
    while True:
        try:
            rounds = int(input("Enter the number of rounds (must be odd): "))
            if rounds % 2 != 0:
                break
            else:
                print("Please enter an odd number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    humanScore, computerScore = 0, 0
    for _ in range(rounds):
        if humanScore > rounds // 2 or computerScore > rounds // 2:
            break
        human = input("Choose your move (Rock, Paper, Scissors): ")
        result = playRound(human)
        print(result)
        if "Human Wins" in result:
            humanScore += 1
        elif "Computer Wins" in result:
            computerScore += 1
    if humanScore > computerScore:
        print("Congratulations! You won the game!")
    else:
        print("The computer wins the game. Better luck next time!")

if __name__ == "__main__":
    main()