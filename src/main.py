# 游戏程序主体

import random
from core.constants import *
from core.board import Board
from core.game import Game
from ai.random import RandomAI
from ai.minimax1 import MinimaxAI1
from ai.minimax2 import MinimaxAI2
from ai.minimax3_ml import ML_MinimaxAI3
from ai.minimax4 import MinimaxAI4
from ai.minimax5_ml import ML_MinimaxAI5
from ai.minimax_ml import ML_MinimaxAI

def main() :
    
    game = Game()
    random_ai = RandomAI()
    ai1 = MinimaxAI1()
    ai2 = MinimaxAI2()
    ai3 = ML_MinimaxAI3()
    ai4 = MinimaxAI4()
    ai5 = ML_MinimaxAI5()
    ml_ai = ML_MinimaxAI()
    start = 2
    # 请自行选择你的AI对手
    print("棋盘大小：", BOARD_SIZE, '*', BOARD_SIZE)
    print("游戏开始，您执黑棋先行：")
    game.print_board()
    while game.game_state == PLAYING : 
        if game.board.current_player == BLACK :
            print("请输入落子位置(0-based):")
            row, col = map(int,input().split())
            while not(game.board.check_valid_move(row,col)) :
                print("落子无效，请重新输入：")
                row, col = map(int,input().split())
            game.make_move(row, col)
        elif start:
            pos = ml_ai.get_start_move(game.board, WHITE)
            game.make_move(pos[0], pos[1])
            start = 0
        else :
            pos = ml_ai.get_move(game.board, WHITE)
            game.make_move(pos[0], pos[1])

if __name__ == "__main__":
    main()