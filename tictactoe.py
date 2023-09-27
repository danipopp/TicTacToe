"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # define variables, count the number
    count_x = 0
    count_o = 0

    # loop through every loop
    for i in range(0,3):
        for j in range(0,3):
            if board(i,j) == X:
                count_x += 1
            elif board(i,j) == O:
                count_o += 1
    # 
    if count_x > count_o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # define return set
    available = set()

    # check where are empty spaces
    for i in range(0,3):
        for j in range(0,3):
            if board(i,j) == EMPTY:
                available.add((i,j))

    return available


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # check if the move is possible
    if action not in actions(board):
        raise ValueError
    # Copy because of the minimax function
    result = board.deepcopy()
    result[action[0],action[1]] = player(board)

    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check the rows
    if all(i==board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i==board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i==board[2][0] for i in board[2]):
        return board[2][0]
    # Check columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    elif len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # if game over no need to calculate anything
    if terminal(board):
        return None
    # if it's gamestart the board starts in the middle
    if len(actions(board)) == 9:
        return ((1,1))
    

    raise NotImplementedError


def maxValue(board):
    # TODO
    raise NotImplementedError

def minValue(board):
    # TODO
    raise NotImplementedError