# 需要实现对当前状态的估价
from core.constants import *

def within_board(row, col) :
    return (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE)

def evaluate(board) :
    # if board.board[4][4] == board.board[4][5] and board.board[4][6] == board.board[4][5] :
    #     print("qwerqefasdf")
    #     print(board.board[4][4])
    #     print(board.features)
    res = -18047
    res += -468107 * board.features[5]
    res += -356700 * board.features[4]
    res += -240863 * board.features[3]
    res += -7548 * board.features[2]
    res += 911150 * board.features[11]
    res += 183394 * board.features[10]
    res += 88437 * board.features[9]
    res += 6492 * board.features[8]
    # if res != -18047 : 
    #     print("res = ",res)
    return res