# Minimax Tic Tac Toe

Tic tac toe against an opponent that cannot lose, with a Pygame front end. The interesting
half is `tictactoe.py`, which holds the rules and the search. `runner.py` is just the
window, the board drawing and the mouse handling.

## What it does

Click to play as X or O, then click an empty square to move. X always goes first. The
computer replies about half a second later, and when the game ends there is a Play Again
button. The best result available to you is a draw. If you lose, you made a mistake
somewhere, because the computer never will.

## How the AI works

Minimax plays the entire rest of the game in its head before committing to a move. Starting
from the current board it tries every legal move, then every reply to each of those, and
keeps recursing until each imagined game is finished, scoring the finished boards +1 if X
won, -1 if O won and 0 for a draw. Those scores then get carried back up the tree on the
assumption that each player picks the branch that suits them, so X takes the highest value
available and O takes the lowest, and every position ends up worth whatever the player to
move would actually choose. The computer plays the move that survives that process, which
is why it never walks into a line a perfect opponent could punish.

There is no alpha-beta pruning here. Tic tac toe has at most 9! = 362,880 move orderings
from an empty board, so searching all of them takes well under a second and the extra code
would not buy anything. The half-second pause before the computer moves is deliberate,
without it the reply lands so fast the game feels broken.

## Running it

You need Python 3 and Pygame.

```bash
pip install pygame
python runner.py
```

One thing to sort out first: `runner.py` loads `OpenSans-Regular.ttf` from its own folder,
and that file is not in this repository. Download Open Sans, drop the regular weight `.ttf`
next to `runner.py` under exactly that name, or the game dies on startup before the window
appears.

## Current state

It works and I have not found a way to beat it. Two rough edges I know about:

- Mouse input is read by polling `pygame.mouse.get_pressed()` every frame rather than
  handling click events, so `time.sleep(0.2)` is used as a debounce on the side-select and
  Play Again buttons. It works, but it is a hack and it stalls the whole loop.
- There is no keyboard control and no way to quit other than closing the window.

## Tech

Python 3 and Pygame. MIT licensed, see LICENSE.
