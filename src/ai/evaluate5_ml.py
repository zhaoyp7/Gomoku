# 需要实现对当前状态的估价
from core.constants import *

def within_board(row, col) :
    return (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE)

def evaluate(board) :
    # val = [-30  , -200  , -500, -3000  , -7000, -300000  , 20  , 150  ,300  , 2000  , 5000  , 200000]
    val = [-32.7, -221.9, -515, -2975.6, -6490, -297905.9, 22.7, 164.4, 315.9, 2028.3, 5183.3, 202437.9]
    res = 5.94
    for i in range(12) :
        res += val[i] * board.features[i]
    # print(res)
    return int(res)