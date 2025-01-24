import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.user_player = "X"
        self.computer_player = "O"
        self.board = [""] * 9
        self.buttons = []

        # Create the selection screen for choosing X or O
        self.create_selection_screen()

    def create_selection_screen(self):
        # Frame for the selection screen
        self.selection_frame = tk.Frame(self.root)
        self.selection_frame.pack()

        # Label and buttons for selecting X or O
        tk.Label(self.selection_frame, text="Choose your mark:").pack()
        tk.Button(self.selection_frame, text="X", command=lambda: self.start_game("X")).pack(side=tk.LEFT)
        tk.Button(self.selection_frame, text="O", command=lambda: self.start_game("O")).pack(side=tk.RIGHT)

    def start_game(self, user_player):
        # Set the user and computer players based on the selection
        self.user_player = user_player
        self.computer_player = "O" if user_player == "X" else "X"
        # Remove the selection screen
        self.selection_frame.destroy()
        # Create the game board
        self.create_board()

    def create_board(self):
        # Create a 3x3 grid of buttons for the game board
        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        # If the computer is X, make the first move
        if self.computer_player == "X":
            self.computer_move()

    def on_button_click(self, index):
        # Handle the user's move
        if self.board[index] == "" and self.current_player == self.user_player:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            # Check for a winner or draw
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_game()
            else:
                # Switch to the computer's turn
                self.current_player = self.computer_player
                self.computer_move()

    def computer_move(self):
        # Handle the computer's move
        available_moves = [i for i, x in enumerate(self.board) if x == ""]
        if available_moves:
            index = random.choice(available_moves)
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            # Check for a winner or draw
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_game()
            else:
                # Switch to the user's turn
                self.current_player = self.user_player

    def check_winner(self):
        # Check for a winning combination
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != "":
                return True
        return False

    def reset_game(self):
        # Reset the game board for a new game
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"
        if self.computer_player == "X":
            self.computer_move()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()