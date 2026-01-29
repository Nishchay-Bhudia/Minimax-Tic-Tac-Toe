
#Tic Tac Toe Player
#Uses the minimax algorithm to choose the optimal move

#imports
import math

#basic variables
X = "X"
O = "O"
EMPTY = None


def initial_state():
    
    #Returns starting state of the board.
    
    # 3x3 grid initialised with EMPTY values
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]


def player(board):
    
    #Returns player who has the next turn on a board.
    
    #X always starts first
    if board == initial_state():
        return X

    # Count number of moves played by each player
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    #If X has played more moves, it must be O's turn
    if x_count > o_count:
        return O
    return X


def actions(board):
    
    #Returns set of all possible actions (i, j) available on the board.
    
    moves = set()

    # Loop through board to find empty cells
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                moves.add((i, j))

    return moves


def result(board, action):
    
    #Returns the board that results from making move (i, j) on the board.
    i, j = action

    # Prevent overwriting an existing move
    if board[i][j] is not EMPTY:
        raise Exception("Invalid move")

    # Create a copy of the board to avoid modifying original
    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)

    return new_board


def winner(board):
    
    #Returns the winner of the game, if there is one.
    
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    return None


def terminal(board):
    
    #Returns True if game is over, False otherwise.
    # Game is over if there is a winner
    if winner(board) is not None:
        return True

    # Game continues if at least one empty space exists
    for row in board:
        for cell in row:
            if cell is EMPTY:
                return False

    # No empty spaces and no winner then it is a draw
    return True


def utility(board):
    
    #Returns 1 if X has won, -1 if O has won, 0 otherwise.
    result = winner(board)

    if result == X:
        return 1
    if result == O:
        return -1
    return 0


def minimax(board):      # the main function (brains of the AI) 
    
    #Returns the optimal action for the current player.
    # No move needed if game already finished
    if terminal(board):
        return None

    current_player = player(board)

    # X aims to maximise the score
    if current_player == X:
        best_score = -math.inf
        best_move = None

        for move in actions(board):
            score = min_value(result(board, move))
            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    # O aims to minimise the score
    else:
        best_score = math.inf
        best_move = None

        for move in actions(board):
            score = max_value(result(board, move))
            if score < best_score:
                best_score = score
                best_move = move

        return best_move


def max_value(board):
    # Returns maximum utility value for X
    if terminal(board):
        return utility(board)

    value = -math.inf
    for move in actions(board):
        value = max(value, min_value(result(board, move)))
    return value


def min_value(board):
    # Returns minimum utility value for O
    if terminal(board):
        return utility(board)

    value = math.inf
    for move in actions(board):
        value = min(value, max_value(result(board, move)))
    return value
