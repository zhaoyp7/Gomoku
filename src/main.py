# 游戏程序主体
import random
from core.constants import *
from core.board import Board
from core.game import Game
from ai.random import RandomAI
from ai.minimax2 import MinimaxAI2
from ai.minimax1 import MinimaxAI1
from ai.minimax5_ml import ML_MinimaxAI
from ai.minimax4 import MinimaxAI4

def main() :
    print(BOARD_SIZE)
    game = Game()
    ai2 = MinimaxAI2()
    ai1 = MinimaxAI1()
    ai4 = MinimaxAI4()
    random_ai = RandomAI()
    ml_ai = ML_MinimaxAI()
    start = 2
    while game.game_state == PLAYING : 
        if game.board.current_player == BLACK :
            print("请输入落子位置")
            row, col = map(int,input().split())
            while not(game.board.check_valid_move(row,col )) :
                print("落子无效，请重新输入：")
                row, col = map(int,input().split())
            game.make_move(row, col)
            # if start :
            #     pos = random_ai.get_move(game.board)
            # else :
            #     pos = ai1.get_move(game.board, BLACK)
            # game.make_move(pos[0], pos[1])
        elif start:
            pos = ml_ai.get_start_move(game.board, WHITE)
            game.make_move(pos[0], pos[1])
            start = 0
        else :
            pos = ml_ai.get_move(game.board, WHITE)
            game.make_move(pos[0], pos[1])

if __name__ == "__main__":
    main()