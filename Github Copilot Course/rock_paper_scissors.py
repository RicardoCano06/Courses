"""
This module implements a Rock Paper Scissors game with a graphical user interface (GUI) using Tkinter.
Classes:
    RockPaperScissorsGUI: A Tkinter-based GUI class that allows the player to play Rock Paper Scissors against the computer.
        - Tracks player and computer scores.
        - Displays the result of each round.
        - Allows the player to quit the game.
Functions:
    add_numbers(a, b): Returns the sum of two numbers a and b.
Usage:
    Run the module to start the Rock Paper Scissors GUI game. The player can select Rock, Paper, or Scissors, and the computer will randomly select its move. The game displays the result of each round and keeps score until the player chooses to quit.
Create a Rock Paper Scissors game where the player inputs their choice
and plays  against a computer that randomly selects its move, 
with the game showing who won each round.
Add a score counter that tracks player and computer wins, 
and allow the game to continue until the player types “quit”.
"""
import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissorsGUI:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")
        master.configure(bg="#f0e68c")  # Fondo principal colorido

        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0
        self.tie_score = 0  # Track number of ties

        self.label = tk.Label(master, text="Choose Rock, Paper, or Scissors:", bg="#f0e68c", fg="#2e4053", font=("Arial", 14, "bold"))
        self.label.pack(pady=10)

        self.button_frame = tk.Frame(master, bg="#f0e68c")
        self.button_frame.pack()

        self.rock_button = tk.Button(self.button_frame, text="Rock", width=10, bg="#ff7675", fg="white", font=("Arial", 12, "bold"), command=lambda: self.play_round("rock"))
        self.rock_button.grid(row=0, column=0, padx=5)

        self.paper_button = tk.Button(self.button_frame, text="Paper", width=10, bg="#74b9ff", fg="white", font=("Arial", 12, "bold"), command=lambda: self.play_round("paper"))
        self.paper_button.grid(row=0, column=1, padx=5)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", width=10, bg="#55efc4", fg="white", font=("Arial", 12, "bold"), command=lambda: self.play_round("scissors"))
        self.scissors_button.grid(row=0, column=2, padx=5)

        self.result_label = tk.Label(master, text="", bg="#f0e68c", font=("Arial", 13, "bold"))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(master, text="Player: 0  Computer: 0  Ties: 0", bg="#f0e68c", fg="#2d3436", font=("Arial", 12, "bold"))
        self.score_label.pack(pady=5)

        self.quit_button = tk.Button(master, text="Quit", bg="#636e72", fg="white", font=("Arial", 11, "bold"), command=master.quit)
        self.quit_button.pack(pady=5)

    def play_round(self, player_choice):
        """
        Play a round of Rock Paper Scissors.

        Args:
            player_choice (str): The player's choice, must be 'rock', 'paper', or 'scissors'.
        """
        computer_choice = random.choice(self.choices)
        result = ""
        color = "#2d3436"  # Default color
        if player_choice == computer_choice:
            result = f"Both chose {player_choice}. It's a tie!"
            self.tie_score += 1
            color = "#fdcb6e"  # Amarillo para empate
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            result = f"You chose {player_choice}, computer chose {computer_choice}. You win!"
            self.player_score += 1
            color = "#00b894"  # Verde para ganar
        else:
            result = f"You chose {player_choice}, computer chose {computer_choice}. You lose!"
            self.computer_score += 1
            color = "#d63031"  # Rojo para perder
        self.result_label.config(text=result, fg=color)
        self.score_label.config(
            text=f"Player: {self.player_score}  Computer: {self.computer_score}  Ties: {self.tie_score}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGUI(root)
    root.mainloop()