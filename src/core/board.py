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
        self.features = np.zeros(12, dtype=int)
        # 眠二 活二 眠三 活三(and _oo_o) 冲四(and 跳四) 活四
        # upd: 放弃记录 _oo_o and 跳四

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
        mid = BOARD_SIZE // 2
        bin = [[0 for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
        q = []
        list = []
        for i in range(0,BOARD_SIZE) :
            for j in range(0,BOARD_SIZE) :
                if self.board[i][j] != EMPTY: 
                    bin[i][j] = 1
                    q.append([i,j])
        if len(q) == 0 :
            q.append([mid,mid])
            list.append([mid,mid])
        head = 0
        while head < len(q) :
            x,y = q[head]
            head += 1
            for dx,dy in [[1,0], [-1,0], [0,1], [0,-1]] :
                if within_board(x + dx,y + dy) and bin[x + dx][y + dy] == 0 :
                    bin[x + dx][y + dy] = 1
                    list.append([x + dx,y + dy])
                    q.append([x + dx,y + dy])
        # print(list)
        return  list



        list_all = [[] for i in range(BOARD_SIZE)]
        list = []
        for i in range(0,BOARD_SIZE) :
            for j in range(0,BOARD_SIZE) :
                if self.check_valid_move(i, j) : 
                    mid = BOARD_SIZE // 2
                    dis = max(abs(i - mid),abs(j - mid))
                    list_all[dis].append([i,j])
        for i in range(BOARD_SIZE) :
            for j in range(len(list_all[i])) :
                list.append(list_all[i][j])
        # print(list)
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
                if list[i] == EMPTY or cnt < 2 or op == 0 or cnt > 4:
                    continue
                tmp = (cnt - 2) * 2 + op - 1
                if list[i] == WHITE :
                    tmp += 6
                self.features[tmp] += val

        # for i in range(len(list)) : 
        #     color = list[i]
        #     if i + 4 < len(list) and list[i] == list[i + 4] and list[i] != EMPTY:
        #         cnt = 0
        #         empty_count = 0
        #         for j in range(i + 1,i + 4) :
        #             if list[j] == color :
        #                 cnt += 1
        #             elif list[j] == EMPTY :
        #                 empty_count += 1
        #         if cnt + empty_count == 3 and empty_count == 1 :
        #             if color == BLACK :
        #                 self.features[4] += val
        #             else :
        #                 self.features[10] += val
        
        # for i in range(len(list)) : 
        #     color = list[i]
        #     if i + 3 < len(list) and list[i] == list[i + 3] and list[i] != EMPTY:
        #         cnt = 0
        #         empty_count = 0
        #         for j in range(i + 1,i + 3) :
        #             if list[j] == color :
        #                 cnt += 1
        #             elif list[j] == EMPTY :
        #                 empty_count += 1
        #         op = 0
        #         if i != 0 and list[i - 1] == EMPTY :
        #             op += 1
        #         if i + 4 < len(list) and list[i + 4] == EMPTY :
        #             op += 1
        #         if cnt == 1 and empty_count == 1 and op:
        #             if color == BLACK :
        #                 self.features[3] += val
        #             else :
        #                 self.features[9] += val
    
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
        