# Kevin Beaghan 4/6/2025
# [COMS 1270 A] Week 12 Lab - Using pytest to fix the fourinSequence code using unit tests from assignment 4

import pytest

from fourInSequence import checkForNextMoveWin
def test_checkForNextMoveWin():
    pass

from fourInSequence import checkAdjacent
def test_checkAdjacent():
    pass

from fourInSequence import checkDraw
def test_checkDraw():
    pass

from fourInSequence import checkWinner
def test_checkWinner():
    pass

# import pytest
# from fourInSequence import checkForNextMoveWin, checkAdjacent, checkDraw, checkWinner, createBoard, dropPieceIntoBoard

# def test_checkForNextMoveWin():
#     board = createBoard(7, 6)  # Create an empty board
#     dropPieceIntoBoard(board, 0, 1)  # Player 1 places a piece in column 0
#     dropPieceIntoBoard(board, 1, 1)  # Player 1 places a piece in column 1
#     dropPieceIntoBoard(board, 2, 1)  # Player 1 places a piece in column 2
#     assert checkForNextMoveWin(board, 1) == 3  # Player 1 has a winning move in column 3

# def test_checkAdjacent():
#     board = createBoard(7, 6)  # Create an empty board
#     dropPieceIntoBoard(board, 0, 1)  # Player 1 places a piece in column 0
#     dropPieceIntoBoard(board, 1, 1)  # Player 1 places a piece in column 1
#     assert checkAdjacent(board, 1) in [0, 1]  # Check adjacent columns

# def test_checkDraw():
#     board = createBoard(7, 6)
#     for col in range(7):
#         for _ in range(6):  # Fill the board completely
#             dropPieceIntoBoard(board, col, 1 if col % 2 == 0 else 2)
#     assert checkDraw(board) == True  # Full board means it's a draw

# def test_checkWinner_horizontal():
#     board = createBoard(7, 6)
#     for i in range(4):  # Place pieces horizontally
#         dropPieceIntoBoard(board, i, 1)
#     assert checkWinner(board, 1) == True  # Player 1 wins horizontally

# def test_checkWinner_vertical():
#     board = createBoard(7, 6)
#     for _ in range(4):  # Place pieces vertically in column 0
#         dropPieceIntoBoard(board, 0, 1)
#     assert checkWinner(board, 1) == True  # Player 1 wins vertically

# def test_checkWinner_diagonal():
#     board = createBoard(7, 6)
#     dropPieceIntoBoard(board, 0, 1)
#     dropPieceIntoBoard(board, 1, 2)
#     dropPieceIntoBoard(board, 1, 1)
#     dropPieceIntoBoard(board, 2, 2)
#     dropPieceIntoBoard(board, 2, 2)
#     dropPieceIntoBoard(board, 2, 1)
#     dropPieceIntoBoard(board, 3, 2)
#     dropPieceIntoBoard(board, 3, 2)
#     dropPieceIntoBoard(board, 3, 2)
#     dropPieceIntoBoard(board, 3, 1)
#     assert checkWinner(board, 1) == True  # Player 1 wins diagonally