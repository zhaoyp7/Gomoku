# 需要实现对当前状态的估价
from core.constants import *

def within_board(row, col) :
    return (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE)

def evaluate(board) :
    # val = [-30  , -200  , -500, -3000  , -7000, -300000  , 20  , 150  ,300  , 2000  , 5000  , 200000]
    val = [-27.3, -202.4, -496.2, -2960.4, -7513.8, -302146.8, 14.1, 140.3, 302.7, 1997.7, 5123.5, 202392.5]
    res = 5.94
    for i in range(12) :
        res += val[i] * board.features[i]
    # print(res)
    return int(res)