#!/usr/bin/env python

from copy import deepcopy

CONFIG = "settings.json"
BLOCK = -5
EMPTY = -1
HEIGHT = 8
WIDTH = 6
POINTS = [(2,1), (4,2), (3,3), (5,4), (2,5), (5,5), (4,6)]
START = (3,0)
END = (HEIGHT * WIDTH) - len(POINTS)

def create_board(height, width, block_list):
    """ Given a height, width, and list of tuple points, creates a create_board
        of zeros then places blocks as BLOCK value """
    board = [[EMPTY for i in range(width)] for i in range(height)]
    for point in block_list:
        board[point[1]][point[0]] = BLOCK
    return board

def solve(board, point, end, turns):
    invalid_x = point[0] < 0 or point[0] >= len(board[0])
    invalid_y = point[1] < 0 or point[1] >= len(board)
    if invalid_x or invalid_y:
        print("Invalid coords")
        return (False, board)
    value = board[point[1]][point[0]]
    if value != EMPTY:
        return (False, board)

    board[point[1]][point[0]] = turns
    format_board(board)

    if turns == end:
        return (True, board)

    up = solve(deepcopy(board), (point[0], point[1] - 1), end, turns + 1)
    if up[0]:
        return up
    down = solve(deepcopy(board), (point[0], point[1] + 1), end, turns + 1)
    if down[0]:
        return down
    left = solve(deepcopy(board), (point[0] - 1, point[1]), end, turns + 1)
    if left[0]:
        return left
    right = solve(deepcopy(board), (point[0] + 1, point[1]), end, turns + 1)
    if right[0]:
        return right

    print("Trapped")
    return (False, board)


def format_board(board):
    """ Creates string representation of board """
    print("")
    for row in board:
        print("[" + " ,".join(["%3d" % x for x in row]) + "]")
    print("")
    
def main():
    board = create_board(HEIGHT, WIDTH, POINTS)
    answer = solve(deepcopy(board), START, END, 1)[1]
    format_board(answer)

if __name__ == '__main__':
    main()
