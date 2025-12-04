# 需要实现游戏的基本逻辑判断

from .board import Board
from .constants import *

# 实现一个 Game 类，维护以下信息
# size : 棋盘大小
# board : 当前棋盘
# game_state : 当前游戏状态

# 实现以下函数
# __init__(self) : 初始化
# make_move(self, row, col) : 调用 Board 实现落子，并且判断落子后游戏状态
# print_board(self) : 输出棋盘
# print_result(self) : 打印游戏结果

class Game:

    def __init__(self):
        self.board = Board()
        self.size = BOARD_SIZE
        self.game_state = PLAYING

    def print_board(self):
        """打印棋盘状态"""
        symbols = {BLACK: '●', WHITE: '○', EMPTY: '·'}
        print("  ", end="")
        for col in range(BOARD_SIZE):
            print(f"{col:2d}", end="")
        print()

        for row in range(BOARD_SIZE):
            print(f"{row:2d} ", end="")
            for col in range(BOARD_SIZE):
                print(symbols[self.board.board[row][col]], end=" ")
            print()
        # print("features",self.board.features)

    def print_result(self):
        """打印游戏结果"""
        if self.game_state == PLAYING:
            print("游戏仍在进行中")
        else:
            print("\n游戏结束：", end="")
            if self.game_state == BLACK_WIN:
                print("黑方获胜!")
            elif self.game_state == WHITE_WIN:
                print("白方获胜!")
            elif self.game_state == DRAW:
                print("平局！棋盘已满。")
        return

    def make_move(self, row, col):
        """落子。"""
        self.board.place_stone(row, col)
        self.print_board()
        if self.board.check_win(row, col) : 
            self.game_state = self.board.game_state
        elif self.board.check_full() :
            self.game_state = DRAW
        self.print_result()