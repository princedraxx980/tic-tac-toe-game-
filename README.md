🎮 Tic Tac Toe - Python GUI Game
A fun and interactive Tic Tac Toe game built using Python and Tkinter, where you play as "X" against a basic AI (computer as "O"). The game keeps score, provides visual feedback, and offers an engaging graphical interface.

📌 Features
🎨 Graphical User Interface using Tkinter
🤖 Single-player mode: You vs Computer
🧠 Basic AI logic: Blocks player wins and plays optimally
🧾 Score tracking for both Player and Computer
🔁 Automatic board reset after each round
💡 Game-over prompts for win/draw conditions

🖼️ Demo
<img src="assets/demo.png" alt="Tic Tac Toe Screenshot" width="400">

🛠️ Technologies Used
Python 3.x
Tkinter (built-in Python GUI library)
random module for AI move selection

🚀 Getting Started
🔧 Prerequisites
Python 3.x installed on your machine

📦 Installation
Clone the repository:
git clone https://github.com/yourusername/tic-tac-toe-gui.git
cd tic-tac-toe-gui

Run the game:
python tic_tac_toe_gui.py

🎮 How to Play
You play as "X", computer plays as "O"
Click on a grid cell to make your move
The AI will respond after a brief delay
The first to align three symbols wins
If the board fills without a winner, it’s a draw
The score updates after every round

🧠 AI Strategy
The computer chooses its moves based on the following priority:
Win if possible
Block player's winning move
Take corners
Take center
Take any remaining spot

🧾 File Overview
tic_tac_toe_gui.py: Main script containing the full game logic and GUI
Uses object-oriented programming via the TicTacToe class

🔮 Future Enhancements
Add difficulty levels (Easy/Medium/Hard)
Add player name input and save high scores
Add sound effects and animations
Export scores to a local file

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
