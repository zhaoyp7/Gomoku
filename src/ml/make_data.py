# 游戏程序主体

import sys
import os
# 添加src目录到Python路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import random
from core.board import Board
from core.constants import *
from core.game import Game
from ai.random import RandomAI
from ai.minimax import MinimaxAI
from ai.weak_minimax import weak_MinimaxAI
from ai.weak_evaluate import *

def main() :
    # print(BOARD_SIZE)
    game = Game()
    ai = MinimaxAI()
    weak_ai = weak_MinimaxAI()
    random_ai = RandomAI()
    start = 1
    while game.game_state == PLAYING : 
        if start or random.randrange(1, 5) == 1:
            pos = random_ai.get_move(game.board)
            game.make_move(pos[0], pos[1])
            start = 0
        elif game.board.current_player == BLACK :
            pos = ai.get_move(game.board, BLACK)
            game.make_move(pos[0], pos[1])
        else :
            pos = weak_ai.get_move(game.board, WHITE)
            game.make_move(pos[0], pos[1])
        list = []
        for i in range(len(game.board.features)) :
            list.append(int(game.board.features[i]))
        list.append(evaluate(game.board))
        if game.game_state == PLAYING : 
            print(list)

if __name__ == "__main__":
    for _ in range(10000) :
        main()