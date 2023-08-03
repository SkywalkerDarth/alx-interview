#!/usr/bin/python3


""" The N queens puzzle """


import sys


def is_safe(board, row, col):
    """ is_safe
    Args: board, row, col
    Return
        True
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
        if row - i - 1 >= 0 and board[row - i - 1][col - i - 1] == 1:
            return False
        if row + i + 1 < len(board) and board[row + i + 1][col - i - 1] == 1:
            return False
    return True

def solve_nqueens(board, col, n):
    """ solve n_queens
    Args: board, col, n
    Return: bool
    """
    if col == n:
        print_solution(board)
        return

    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1, n)
            board[i][col] = 0

def print_solution(board):
    """ prints out solution """
    for row in board:
        print(' '.join(str(cell) for cell in row))

def main():
    """main file"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    main()
