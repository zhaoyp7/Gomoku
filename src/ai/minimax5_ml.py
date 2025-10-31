import random
import copy
from .evaluate5_ml import *
from core.board import Board
from core.constants import *
# 实现一个基于 Minimax 算法的 AI
empty_move = [-1, -1]

def within_board(row, col) :
    return (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE)

def debug(board) :
    """打印棋盘状态"""
    symbols = {BLACK: '●', WHITE: '○', EMPTY: '·'}
    print("  ", end="")
    for col in range(BOARD_SIZE):
        print(f"{col:2d}", end="")
    print()
    for row in range(BOARD_SIZE):
        print(f"{row:2d} ", end="")
        for col in range(BOARD_SIZE):
            print(symbols[board.board[row][col]], end=" ")
        print()

class ML_MinimaxAI :
    def minimax(self, limit_depth, player, board, lastrow, lastcol, alpha, beta) : 
        if lastrow != -1 and board.check_win(lastrow, lastcol) :
            if player == WHITE :
                return -100000000 * (limit_depth + 1), empty_move
            else : 
                return 100000000 * (limit_depth + 1), empty_move
        if limit_depth == 0 :
            return evaluate(board), empty_move
        list = board.get_valid_pos()
        move = -1, -1
        for pr, pc in list :
            new_board = copy.deepcopy(board)
            new_board.place_stone(pr, pc)
            if player == WHITE :
               val, tmp = self.minimax(limit_depth - 1, 3 - player, new_board, pr, pc, alpha, INF)
            else :
                val, tmp = self.minimax(limit_depth - 1, 3 - player, new_board, pr, pc, -INF, beta)
            if player == WHITE and val > alpha:
                alpha = val
                move = pr, pc
            elif player == BLACK and val < beta :
                beta = val
                move = pr, pc
            if player == WHITE and alpha >= beta :
                return alpha, move
            elif player == BLACK and beta <= alpha :
                return beta, move
        if player == BLACK :
            return beta, move
        else :
            return alpha, move

    def get_move(self, board, color) :
        val, move = self.minimax(2, color, board, -1, -1, -INF, INF)
        # print(move)
        return move

    def get_start_move(self, board, color) :
        mid = BOARD_SIZE // 2
        if color == BLACK :
            if board.board[mid][mid] == EMPTY :
                move = [mid, mid]
            else :
                move = [mid - 1, mid - 1]
            return move
        elif color == WHITE :
            for i in range(BOARD_SIZE) :
                for j in range(BOARD_SIZE) : 
                    if board.board[i][j] != EMPTY :
                        x = i
                        y = j
            list = []
            for i in {-1, 0 ,1} :
                for j in {-1 ,0 ,1} :
                    if within_board(x + i,y + j) and board.board[x + i][y + j] == EMPTY :
                        list.append([x + i,y + j])
            move = list[0]
            for x, y in list :
                if abs(x - mid) + abs(y - mid) < abs(move[0] - mid) + abs(move[1] - mid) :
                    move = [x,y]
            return move
            