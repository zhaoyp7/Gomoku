# 需要实现对当前状态的估价
from core.constants import *

def within_board(row, col) :
    return (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE)

def evaluate(board) :

    res = 0
    res += -30 * board.features[0]
    res += -200 * board.features[1]
    res += -500 * board.features[2]
    res += -3000 * board.features[3]
    res += -7000 * board.features[4]
    res += -15000 * board.features[5]
    res += 20 * board.features[6]
    res += 150 * board.features[7]
    res += 300 * board.features[8]
    res += 2000 * board.features[9]
    res += 5000 * board.features[10]
    res += 10000 * board.features[11]

    # print(res)
    return res