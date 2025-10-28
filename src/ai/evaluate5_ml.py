# 需要实现对当前状态的估价
from core.constants import *

def within_board(row, col) :
    return (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE)

def evaluate(board) :
    # val = [-30  , -200  , -500, -3000  , -7000, -300000  , 20  , 150  ,300  , 2000  , 5000  , 200000]
    val = [-27.3, -178.1, -485, -3024.4, -7510, -302094.1, 17.3, 135.6,284.1, 1971.7, 4816.7, 197562.1]
    res = -5.94
    for i in range(12) :
        res += val[i] * board.features[i]
    # print(res)
    return int(res)