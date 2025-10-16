# 需要实现棋盘的基本操作
# 使用 numpy 模块作为棋盘

# 实现一个 Board 类，维护以下信息：
# size : 棋盘大小
# board : 当前棋盘
# current_player ： 当前玩家

# 实现以下函数
# __init__(self) : 初始化
# CheckWin(self) : 检查是否胜利
# CheckFull(self) : 检查棋盘是否已满
import numpy as np
from .constants import *


class Board:
    def __init__(self):
        self.size = BOARD_SIZE
        self.board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
        self.current_player = BLACK
        self.game_state = PLAYING

    def check_valid_move(self, row, col) :
        if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
            return False
        if self.board[row][col] != EMPTY:
            return False
        return True

    def place_stone(self, row, col):
        """在指定位置放置棋子"""
        self.board[row][col] = self.current_player
        self.current_player = WHITE if self.current_player == BLACK else BLACK

    def check_win(self, row, col):
        """检查新落子是否获胜"""
        player = self.board[row][col]
        if player == EMPTY:
            return False

        # 检查四个方向：水平、垂直、对角线、反对角线
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1  # 当前位置已有一个棋子

            # 正向检查
            r, c = row + dr, col + dc
            while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board[r][c] == player:
                count += 1
                r += dr
                c += dc

            # 反向检查
            r, c = row - dr, col - dc
            while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board[r][c] == player:
                count += 1
                r -= dr
                c -= dc
            # 五子连珠
            if count >= 5:
                self.game_state = BLACK_WIN if player == BLACK else WHITE_WIN
                return True
        return False

    def check_full(self):
        """检查棋盘是否已满"""
        return np.all(self.board != EMPTY)