import random
# from ..core.constants import *

class RandomAI : 
    def get_move(self, board) :
        list = board.get_valid_pos()
        return random.choice(list)
        