"""
Create a Rock Paper Scissors game where the player inputs their choice
and plays  against a computer that randomly selects its move, 
with the game showing who won each round.
Add a score counter that tracks player and computer wins, 
and allow the game to continue until the player types "quit".
"""
import random
import sys

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    if player == computer:
        return 'tie'
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return 'player'
    else:
        return 'computer'

def console_main():
    player_score = 0
    computer_score = 0
    while True:
        player_choice = input("Enter rock, paper, scissors or quit to exit: ").strip().lower()
        if player_choice == 'quit':
            print("Thanks for playing!")
            break
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        winner = determine_winner(player_choice, computer_choice)
        if winner == 'player':
            player_score += 1
            print("You win this round!")
        elif winner == 'computer':
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")
        print(f"Score - You: {player_score}, Computer: {computer_score}\n")

# Simple GUI mode (import tkinter only when needed)
def gui_main():
    try:
        import tkinter as tk
        from tkinter import messagebox
    except Exception as e:
        print("Tkinter is not available on this system:", e)
        return

    class RPSGame:
        def __init__(self, master):
            self.master = master
            self.master.title("Rock Paper Scissors")
            self.player_score = 0
            self.computer_score = 0

            self.label = tk.Label(master, text="Choose Rock, Paper, or Scissors:")
            self.label.pack()

            self.rock_button = tk.Button(master, text="Rock", command=lambda: self.play('rock'))
            self.rock_button.pack()

            self.paper_button = tk.Button(master, text="Paper", command=lambda: self.play('paper'))
            self.paper_button.pack()

            self.scissors_button = tk.Button(master, text="Scissors", command=lambda: self.play('scissors'))
            self.scissors_button.pack()

            self.score_label = tk.Label(master, text="Score - You: 0, Computer: 0")
            self.score_label.pack()

        def play(self, player_choice):
            computer_choice = get_computer_choice()
            winner = determine_winner(player_choice, computer_choice)

            if winner == 'player':
                self.player_score += 1
                result = "You win this round!"
            elif winner == 'computer':
                self.computer_score += 1
                result = "Computer wins this round!"
            else:
                result = "It's a tie!"

            messagebox.showinfo("Result", f"Computer chose: {computer_choice}\n{result}")
            self.score_label.config(text=f"Score - You: {self.player_score}, Computer: {self.computer_score}")

    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() in ('gui', '--gui'):
        gui_main()
    else:
        console_main()