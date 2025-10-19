import random
from .evaluate import *
from core.board import Board
from core.constants import *
# 实现一个基于 Minimax 算法的 AI
empty_move = [-1, -1]

class MinimaxAI :
    def Minimax(self, limit_depth, player, board, lastrow, lastcol) : 
        # print(limit_depth,player,lastrow,lastrow)
        if lastrow != -1 and board.check_win(lastrow, lastcol) :
            if player == 2 :
                return -1000000000, empty_move
            else : 
                return 1000000000, empty_move
        if limit_depth == 0 :
            return evaluate(board), empty_move
        list = []
        for i in range(0,board.size) :
            for j in range(0,board.size) :
                if board.check_valid_move(i, j) : 
                    list.append([i,j])
        move = -1, -1
        if player == 2 :
            res = -1000000000
        else :
            res = 1000000000
        # print(list)
        for pos in list :
            # print(board.current_player)
            # print(pos)
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
            val, tmp = self.Minimax(limit_depth - 1, 3 - player, new_board, pos[0], pos[1])
            # print(val,tmp[0],tmp[1],res)
            if player == 2 and val > res:
                res = val
                move = pos
            elif player == 1 and val < res :
                res = val
                move = pos
        return res,move

    def GetMove(self, board) :
        val, move = self.Minimax(1, 2, board, -1, -1)
        return move