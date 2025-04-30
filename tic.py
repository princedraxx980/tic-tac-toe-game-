import random
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        self.player_score = 0
        self.computer_score = 0

        self.player_marker = "X"
        self.computer_marker = "O"
        self.turn = "Player"

        self.create_score_labels()
        self.create_board()
        self.reset_game()

    def create_score_labels(self):
        self.player_score_label = tk.Label(self.master, text=f"Player: {self.player_score}", font=("Arial", 16))
        self.player_score_label.grid(row=3, column=0, columnspan=3, pady=(10, 0))

        self.computer_score_label = tk.Label(self.master, text=f"Computer: {self.computer_score}", font=("Arial", 16))
        self.computer_score_label.grid(row=4, column=0, columnspan=3, pady=(5, 10))

    def create_board(self):
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.master, text=" ", font=("Arial", 40), width=2, height=1,
                               command=lambda pos=i: self.make_move(pos),
                               bg="#f0f0f0", activebackground="#ddd", relief=tk.RAISED, borderwidth=2)
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

    def reset_game(self):
        self.board = [" "] * 9
        self.turn = "Player"
        for button in self.buttons:
            button.config(text=" ", state=tk.NORMAL, bg="#f0f0f0")  # Reset button color

    def make_move(self, position):
        if self.board[position] == " " and self.turn == "Player":
            self.board[position] = self.player_marker
            self.buttons[position].config(text=self.player_marker, state=tk.DISABLED, bg="#e0f2f7")

            if self.check_win(self.player_marker):
                self.update_score(player=True)
                self.game_over("Congratulations! You have won the game!")
            elif self.check_draw():
                self.game_over("The game is a draw!")
            else:
                self.turn = "Computer"
                self.master.after(200, self.computer_move)

    def computer_move(self):
        position = self.computer_choice()
        if position is not None:
            self.board[position] = self.computer_marker
            self.buttons[position].config(text=self.computer_marker, state=tk.DISABLED, bg="#ffe0b2")

            if self.check_win(self.computer_marker):
                self.update_score(player=False)
                self.game_over("The computer has won!")
            elif self.check_draw():
                self.game_over("The game is a draw!")
            else:
                self.turn = "Player"


    def computer_choice(self):  # AI logic (same as before)
        for i in range(9):
            if self.board[i] == " ":
                board_copy = self.board[:]
                board_copy[i] = self.computer_marker
                if self.check_win(self.computer_marker, board_copy):
                    return i

        for i in range(9):
            if self.board[i] == " ":
                board_copy = self.board[:]
                board_copy[i] = self.player_marker
                if self.check_win(self.player_marker, board_copy):
                    return i

        available_corners = [i for i in [0, 2, 6, 8] if self.board[i] == " "]
        if available_corners:
            return random.choice(available_corners)

        if self.board[4] == " ":
            return 4

        available_spaces = [i for i in range(9) if self.board[i] == " "]
        if available_spaces:
            return random.choice(available_spaces)
        return None

    def check_win(self, mark, board=None):
        if board is None:
            board = self.board
        return ((board[0] == mark and board[1] == mark and board[2] == mark) or
                (board[3] == mark and board[4] == mark and board[5] == mark) or
                (board[6] == mark and board[7] == mark and board[8] == mark) or
                (board[0] == mark and board[3] == mark and board[6] == mark) or
                (board[1] == mark and board[4] == mark and board[7] == mark) or
                (board[2] == mark and board[5] == mark and board[8] == mark) or
                (board[0] == mark and board[4] == mark and board[8] == mark) or
                (board[2] == mark and board[4] == mark and board[6] == mark))

    def check_draw(self):
        return " " not in self.board

    def update_score(self, player):
        if player:
            self.player_score += 1
            self.player_score_label.config(text=f"Player: {self.player_score}")
        else:
            self.computer_score += 1
            self.computer_score_label.config(text=f"Computer: {self.computer_score}")

    def game_over(self, message):
        for button in self.buttons:
            button.config(state=tk.DISABLED)

        result = messagebox.showinfo("Game Over", message)
        if result:
            self.reset_game()

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()