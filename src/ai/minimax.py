import random
from .evaluate import *
from core.board import Board
from core.constants import *
# 实现一个基于 Minimax 算法的 AI
empty_move = [-1, -1]

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

class MinimaxAI :
    def minimax(self, limit_depth, player, board, lastrow, lastcol, alpha, beta) : 
        # debug(board)
        # print(limit_depth,player,lastrow,lastcol)
        if lastrow != -1 and board.check_win(lastrow, lastcol) :
            if player == 2 :
                return -INF, empty_move
            else : 
                return INF, empty_move
        if limit_depth == 0 :
            return evaluate(board), empty_move
        list = []
        for i in range(0,board.size) :
            for j in range(0,board.size) :
                if board.check_valid_move(i, j) : 
                    list.append([i,j])
        move = -1, -1
        if player == 2 :
            res = -INF
        else :
            res = INF
        for pos in list :
            new_board = Board()
            for i in range(BOARD_SIZE) :
                for j in range(BOARD_SIZE) : 
                    if board.board[i][j] == 0 :
                        new_board.board[i][j] = 0
                    elif board.board[i][j] == 1 :
                        new_board.board[i][j] = 1
                    elif board.board[i][j] == 2 :
                        new_board.board[i][j] = 2
            if board.current_player == 1 :
                new_board.current_player = 1
            else :
                new_board.current_player = 2
            new_board.place_stone(pos[0], pos[1])
            if player == 2 :
               val, tmp = self.minimax(limit_depth - 1, 3 - player, new_board, pos[0], pos[1], alpha, INF)
            else :
                val, tmp = self.minimax(limit_depth - 1, 3 - player, new_board, pos[0], pos[1], -INF, beta)
            if player == 2 and val >= alpha:
                alpha = val
                move = pos
            elif player == 1 and val <= beta :
                beta = val
                move = pos
            if player == 2 and alpha >= beta :
                return alpha, move
            elif player == 1 and beta <= alpha :
                return beta, move
        if player == 1 :
            return beta, move
        else :
            return alpha, move

    def get_move(self, board) :
        val, move = self.minimax(2, 2, board, -1, -1, -INF, INF)
        return move