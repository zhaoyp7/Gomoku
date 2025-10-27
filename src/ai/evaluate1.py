# 需要实现对当前状态的估价
from core.constants import *

def within_board(row, col) :
    return (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE)

# 一个比较弱的估价函数的例子
def evaluate(board) :
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    res = 0
    for dr, dc in directions:
        for i in range(BOARD_SIZE) : 
            for j in range(BOARD_SIZE) :
                col = board.board[i][j]
                if col == EMPTY :
                    continue
                if within_board(i - dr, j - dc) and col == board.board[i - dr][j - dc] :
                    continue
                cnt = 0
                r = i
                c = j
                while within_board(r,c) and board.board[r][c] == col :
                    cnt += 1
                    r += dr
                    c += dc
                if col == WHITE : 
                    fl = 10
                else : 
                    fl = -21
                op = 0
                if within_board(i - dr,j - dc) and board.board[i - dr][j - dc] == EMPTY :
                    op += 2
                if within_board(r,c) and board.board[r][c] == EMPTY :
                    op += 2
                if op == 4 :
                    op = 10
                res += fl * op * pow(10,cnt)
    
    return res