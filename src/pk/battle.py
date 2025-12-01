import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import random
from core.constants import *
from core.board import Board
from core.game import Game
from ai.random import RandomAI
from ai.minimax1 import MinimaxAI1
from ai.minimax2 import MinimaxAI2
from ai.minimax3_ml import ML_MinimaxAI3
from ai.minimax4 import MinimaxAI4
from ai.minimax5_ml import ML_MinimaxAI

win = 0
draw = 0
lose = 0

# Automatically conduct 50 AI battles against each other

def main() :
    global win,draw,lose
    game = Game()
    random_ai = RandomAI()
    ai1 = MinimaxAI1()
    ai2 = MinimaxAI2()
    ai3 = ML_MinimaxAI3()
    ai4 = MinimaxAI4()
    ai5 = ML_MinimaxAI()
    start = 2
    step = 0
    while game.game_state == PLAYING : 
        step += 1
        if game.board.current_player == BLACK :
            if start : # Randomly take the first step
                pos = random_ai.get_move(game.board)
            else :
                pos = ai5.get_move(game.board, BLACK)
        elif game.board.current_player == WHITE :
            if start:
                pos = ai1.get_move(game.board, WHITE)
                start = 0
            else :
                pos = ai1.get_move(game.board, WHITE)
        game.make_move(pos[0], pos[1])
        if game.game_state != PLAYING :
            if game.game_state == BLACK_WIN :
                print("BLACK WIN , use step = ",step)
                win += 1
            elif game.game_state == WHITE_WIN :
                print("WHITE WIN , use step = ",step)
                lose += 1
            elif game.game_state == DRAW :
                print("DRAW , use step = ",step)
                draw += 1

if __name__ == "__main__":
    for i in range(50) :
        main()
    print(f"ai5 vs ai1 , the results is {win}-{draw}-{lose}")