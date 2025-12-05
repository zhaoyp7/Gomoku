# 伟大思想小组作业—五子棋
组员：赵也品、王心贝、姚米安

## 简介
这个项目实现了一个简易的五子棋AI，它能作为你的对手玩五子棋。我们采用了Minimax算法来实现，同时用 Alpha-Beta 剪枝进行优化。

更进一步地，我们在上述算法的基础上，让AI自己进行相互对战，获取大量的数据之后，训练了一个基于线性回归的ML模型。

为了更好地测试各个AI的强度，我们进行了一个小型的evaluation，通过相互对战对比各个AI的强度。

## 项目结构
```
Gomoku/
├── README.md
├── requirements.txt
├── doc
│   ├── data
│   │   ├── dataset                   # 训练数据集
│   │   └── train_result              # 训练结果
│   └── pk
│       ├── final_results             # 文件夹，存放最强两个AI的对战结果
│       └── results                   # 文件夹，存放所有五个AI的对战结果
└── src
    ├── ai
    │   ├── evaluate1.py
    │   ├── evaluate2.py
    │   ├── evaluate3_ml.py
    │   ├── evaluate4.py
    │   ├── evaluate5_ml.py
    │   ├── minimax1.py               # 基于第一版估价函数的AI
    │   ├── minimax2.py               # 基于第二版估价函数的AI
    │   ├── minimax3_ml.py            # 在AI1基础上，用基于线性回归的ML模型改进估价函数
    │   ├── minimax4.py               # 基于重写估价函数的AI
    │   ├── minimax5_ml.py            # 在AI5基础上，用基于线性回归的ML模型改进估价函数
    │   ├── minimax_ml.py             # 最终版AI
    │   └── random.py                 # 随机落子AI
    ├── core
    │   ├── board.py                  # 实现棋盘的基本操作
    │   ├── constants.py              # 一些常量定义
    │   └── game.py                   # 实现游戏的基本逻辑判断
    ├── main.py
    ├── ml
    │   ├── make_data.py              # 生成训练数据
    │   └── trainer.py                # 训练ML模型
    └── pk
        └── battle.py
```
## 使用说明
直接运行 src 文件夹中 main.py 即可.
