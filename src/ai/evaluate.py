# 需要实现对当前状态的估价
from core.constants import *

def WithInBoard(row, col) :
    return (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE)
# 一个比较弱的估价函数的例子
def evaluate(board) :
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    res = 0
    for dr, dc in directions:
        for i in range(BOARD_SIZE) : 
            for j in range(BOARD_SIZE) :
                tmp = board.board[i][j]
                if tmp == EMPTY :
                    continue
                if WithInBoard(i - dr, j - dc) and tmp == board.board[i - dr][j - dc] :
                    continue
                cnt = 0
                r = i
                c = j
                while WithInBoard(r,c) and board.board[r][c] == tmp :
                    cnt += 1
                    r += dr
                    c += dc
                if tmp == WHITE : 
                    fl = 10
                else : 
                    fl = -21
                op = 0
                if WithInBoard(i - dr,j - dc) and board.board[i - dr][j - dc] == EMPTY :
                    op += 1
                if WithInBoard(r,c) and board.board[r][c] == EMPTY :
                    op += 1
                res += fl * op * pow(10,cnt)
    
    return res