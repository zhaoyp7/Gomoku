import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import random
from core.constants import *
from core.board import Board
from core.game import Game
from ai.evaluate4 import * 
from ai.random import RandomAI
from ai.minimax2 import MinimaxAI2
from ai.minimax1 import MinimaxAI1
from ai.minimax3_ml import ML_MinimaxAI3
from ai.minimax4 import MinimaxAI4

# Obtain sufficient match data
# [feature0~11, value, player, test_num, step]

def main(test_num) :
    step = 0
    game = Game()
    ai2 = MinimaxAI2()
    ai1 = MinimaxAI1()
    ai4 = MinimaxAI4()
    random_ai = RandomAI()
    ml_ai = ML_MinimaxAI3()
    start = 2
    while game.game_state == PLAYING : 
        if random.randrange(1,120) == 1 :
            pos = random_ai.get_move(game.board)
            game.make_move(pos[0], pos[1])
        elif game.board.current_player == BLACK :
            if start :
                pos = random_ai.get_move(game.board)
            else :
                pos = ai1.get_move(game.board, BLACK)
            game.make_move(pos[0], pos[1])
        elif start:
            pos = ai4.get_start_move(game.board, WHITE)
            game.make_move(pos[0], pos[1])
            start = 0
        else :
            pos = ai4.get_move(game.board, WHITE)
            game.make_move(pos[0], pos[1])
        
        list = []
        for i in range(len(game.board.features)) :
            list.append(int(game.board.features[i]))
        step += 1
        list.append(evaluate(game.board))
        list.append(3 - game.board.current_player)
        list.append(test_num)
        list.append(step)
        if game.game_state == PLAYING : 
            print(list)

if __name__ == "__main__":
    for _ in range(1,201) :
        main(_)