import random
# from ..core.constants import *

class RandomAI : 
    def get_move(self, board) :
        list = []
        for i in range(0,board.size) :
            for j in range(0,board.size) :
                if board.check_valid_move(i, j) : 
                    list.append([i,j])
        return random.choice(list)
        