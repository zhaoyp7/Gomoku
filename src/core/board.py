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

def within_board(row, col) :
    return (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE)

class Board:
    def __init__(self):
        self.size = BOARD_SIZE
        self.board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
        self.current_player = BLACK
        self.game_state = PLAYING
        self.features = np.zeros(8, dtype=int)

    def check_valid_move(self, row, col) :
        if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
            return False
        if self.board[row][col] != EMPTY:
            return False
        return True

    def place_stone(self, row, col):
        """在指定位置放置棋子"""
        self.check_features(row, col, -1)
        self.board[row][col] = self.current_player
        self.check_features(row, col, 1)
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
            while within_board(r,c) and self.board[r][c] == player:
                count += 1
                r += dr
                c += dc

            # 反向检查
            r, c = row - dr, col - dc
            while within_board(r,c) and self.board[r][c] == player:
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

    def get_valid_pos(self) :
        list = []
        for i in range(0,BOARD_SIZE) :
            for j in range(0,BOARD_SIZE) :
                if self.check_valid_move(i, j) : 
                    list.append([i,j])
        return list
    
    def update_features(self, list, val) :
        # print(list)
        last = 0
        for i in range(len(list)) : 
            if i + 1 == len(list) or list[i + 1] != list[i] :
                cnt = i - last + 1
                op = 0
                if last != 0 and list[last - 1] == EMPTY :
                    op += 1
                if i + 1 < len(list) and list[i + 1] == EMPTY :
                    op += 1
                last = i + 1
                if list[i] == EMPTY or cnt <= 2 :
                    continue
                if cnt == 3 and op == 2 :
                    if list[i] == BLACK :
                        self.features[2] += val
                    else :
                        self.features[6] += val
                if cnt == 3 and op == 1 :
                    if list[i] == BLACK :
                        self.features[3] += val
                    else :
                        self.features[7] += val
                if cnt == 4 and op == 2 :
                    if list[i] == BLACK :
                        self.features[0] += val
                    else :
                        self.features[4] += val
                if cnt == 4 and op == 1 :
                    if list[i] == BLACK :
                        self.features[1] += val
                    else :
                        self.features[5] += val
        for i in range(len(list)) : 
            color = list[i]
            if i + 4 < len(list) and list[i] == list[i + 4] and list[i] != EMPTY:
                cnt = 0
                empty_count = 0
                for j in range(i + 1,i + 4) :
                    if list[j] == color :
                        cnt += 1
                    elif list[j] == EMPTY :
                        empty_count += 1
                if cnt + empty_count == 3 and empty_count == 1 :
                    if color == BLACK :
                        self.features[0] += val
                    else :
                        self.features[4] += val

    def check_features(self, row, col, val) :
        list = []
        for i in range(BOARD_SIZE) :
            list.append(self.board[i][col])
        self.update_features(list, val)
        
        list = []
        for j in range(BOARD_SIZE) :
            list.append(self.board[row][j])
        self.update_features(list, val)

        list = []
        for i in range(BOARD_SIZE) :
            if within_board(i, row + col - i) :
                list.append(self.board[i][row + col - i])
        self.update_features(list, val)

        list = []
        for i in range(BOARD_SIZE) :
            if within_board(i, col - row + i) :
                list.append(self.board[i][col - row + i])
        self.update_features(list, val)
        