# 需要实现棋盘的基本操作
# 使用 numpy 模块作为棋盘

import numpy as np
from .constants import *

# 实现一个 Board 类，维护以下信息：
# size : 棋盘大小
# board : 当前棋盘
# current_player ： 当前玩家

# 实现以下函数
# __init__(self) : 初始化
# CheckVaildMove(self, row, col) : 检查能否落子
# MakeMove(self, row, col) : 落子
# CheckWin(self) : 检查是否胜利
# CheckFull(self) : 检查棋盘是否已满