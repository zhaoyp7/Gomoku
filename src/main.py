# 游戏程序主体
from core.constants import *
from core.board import Board
from core.game import Game
from ai.random import RandomAI

def main() :
    print(BOARD_SIZE)
    # return 
    game = Game()
    ai = RandomAI()
    while game.game_state == PLAYING : 
        if game.board.current_player == BLACK :
            print("请输入落子位置")
            row, col = map(int,input().split())
            while not(game.board.check_valid_move(row,col )) :
                print("落子无效，请重新输入：")
                row, col = map(int,input().split())
            game.make_move(row, col)
        else :
            pos = ai.GetMove(game.board)
            game.make_move(pos[0], pos[1])

if __name__ == "__main__":
    main()