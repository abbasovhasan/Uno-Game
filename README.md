
# Uno Game in Python 🃏

This project is a **text-based Uno game** implemented in Python. It allows two players to play the popular Uno card game directly in the terminal, complete with special cards and the ability to handle real game mechanics like Wild cards, Skip, Reverse, and Draw Two.

---

## Features ✨

- A fully functional Uno deck with:
  - Four colors (`Red`, `Blue`, `Green`, `Yellow`)
  - Number cards (`0-9`)
  - Special cards (`Skip`, `Reverse`, `Draw Two`, `Wild`, `Wild Draw Four`)
- Dynamic turn management:
  - Handles special card effects like reversing the turn order and skipping turns.
- **"UNO!" rule**: Alerts when a player has only one card left.
- Handles **deck depletion** by recycling the discard pile.
- Simple terminal-based interface with player prompts.

---

## Setup and Installation ⚙️

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/uno-game.git
   cd uno-game
   ```

2. **Ensure Python is Installed:**

   - This game requires **Python 3.7 or higher**.

   To check your Python version:
   ```bash
   python --version
   ```

3. **Run the Game:**

   ```bash
   python main.py
   ```

   If you're using Mac or Linux:
   ```bash
   python3 main.py
   ```

---

## How to Play 🎮

1. At the start of the game:
   - Each player is dealt 5 cards.
   - One card is placed in the discard pile to begin play.
   - The first player is prompted to make their move.

2. During a player's turn:
   - The player can play a card matching the color or number of the top card on the discard pile.
   - Wild cards can be played at any time, allowing the player to choose the next color.

3. Special cards:
   - **Skip**: Skips the next player's turn.
   - **Reverse**: Reverses the order of play.
   - **Draw Two**: Forces the next player to draw two cards.
   - **Wild**: Lets the player choose the next color.
   - **Wild Draw Four**: Lets the player choose the next color and forces the next player to draw four cards.

4. If a player cannot play a valid card:
   - They must draw one card from the deck.

5. The game ends when a player has no cards left, and they are declared the winner.

---

## Game Rules 📜

- A card is valid to play if:
  - It matches the color of the top card on the discard pile.
  - It matches the number or special type of the top card on the discard pile.
  - It is a Wild or Wild Draw Four card (which can be played on any card).
- If the deck is empty, the discard pile (excluding the top card) is shuffled and used as the new deck.
- Players must play strategically to avoid drawing cards and try to force their opponent to draw instead.

---

## Project Structure 📂

```
uno-game/
│
├── main.py         # Main game logic
└── README.md       # Project documentation
```

---

## Contributions 🤝

Contributions are welcome! Feel free to fork this repository and submit pull requests for:
- Enhancing the game features.
- Adding a graphical interface.
- Implementing AI players for single-player mode.

---

## License 📝

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgments 🙏

Thanks for checking out this Uno game! If you enjoy it, feel free to star the repository and share it with others. 🦒✨
