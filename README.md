# 🎮 Tic Tac Toe AI (Minimax + Pygame)

A fully playable **Tic Tac Toe game with an unbeatable AI**, powered by the **Minimax algorithm** and visualised using **Pygame**.

The AI always plays optimally, meaning:
- You can **never beat it** NEVER ,try it 

- The best you can do is **draw** 


You're not bad at the game... the algorithm is just better

---

## 🧠 Features

- Minimax-based AI (optimal decision making)
- Player vs Computer gameplay
- Clean Pygame UI
- Choose to play as **X** or **O** (**X** always goes first)
- Game-over detection (win / lose / draw)
- Restart button after game ends


## To Play The Game 

1. Clone the repository:

```bash
git clone [YOUR_GITHUB_LINK_HERE] 
```

2. Install Pygame

```bash
pip install pygame
```

3. Run the game:

```bash
python runner.py
```

**Controls:**
   • Use your Mouse to select your side (X or O).

   • Click on any empty square to make your move.

  • Hit the Play Again button once the match ends.





## What is MiniMax?

Imagine Minimax as a little baby playing Tic Tac Toe. But this baby is very smart. **Here’s how it thinks:**

**“I want the most sweets (points)!”**

Minimax is like a greedy baby who wants to win every game. It looks at the board and thinks:

**“If I make this move, how many sweets (points) can I get?”**

**“But the other baby wants to stop me!”**

The other baby (the other player) is also a clever baby. They want to win or at least block me from winning.

So our baby Minimax doesn’t just pick the easiest-looking move. It pretends the opponent is smart too.

**“I’ll try everything!”**

Minimax goes into a fantasy world:

**“What if I put my X here? What will the other baby do next?”**

**“What if I put my X there instead? What happens?”**

It plays all possible games in its head, even the ones far in the future.

**“Hmm… what’s best for me?”**

Once it imagines all possible futures, it scores each ending:

**+1** if it wins - baby Minimax gains sweets!

**0** if it’s a draw - baby Minimax doesnt loose or gain sweets

**-1** if it loses - sweets get taken from baby Minimax

Then it picks the move that gives the best score, knowing the other baby will try to ruin it.

**“I can’t lose!”**

Because it thinks ahead about every possible move, this baby is unbeatable.

Even if the other player is tricky, Minimax will **Never** make a mistake.




## 📜 License

This project is open-source and free to use for learning and experimentation.

## 🤝 Contributing

Feel free to fork the repository and improve the game!  
Suggestions for features, UI, or AI improvements are welcome.



