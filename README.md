# 伟大思想小组项目—五子棋
组员：赵也品、王心贝、姚米安

## 简介
本项目实现了一个具备不同智能水平的五子棋AI对弈系统。我们基于Minimax算法构建AI核心，并引入Alpha-Beta剪枝进行性能优化。

此外，我们还通过自对战生成大量棋局数据，训练了一个基于线性回归的机器学习模型，用于改进AI的评估函数，从而提升其下棋水平。

为全面评估各版本AI的强度，我们设计并执行了一个系统性的对战评估实验，对比分析了不同AI版本之间的胜负表现。

---

## 项目特点
- **算法基础**：采用Minimax搜索算法，结合Alpha-Beta剪枝优化搜索效率。
- **机器学习增强**：通过自对战数据训练线性回归模型，动态优化局面评估函数。
- **多版本AI**：提供了从基础到增强的多个AI版本，包括纯规则型和ML增强型。
- **强度评估**：内置对战系统，可自动化进行多轮AI互搏，并统计胜率与表现。

---

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
    ├── main.py                       # 主程序入口
    ├── ml
    │   ├── make_data.py              # 生成训练数据
    │   └── trainer.py                # 训练ML模型
    └── pk
        └── battle.py                 # 自动对战与结果统计脚本
```
## 快速开始

### 环境要求
- Python 3.7+
- 依赖库：见 `requirements.txt`

### 安装依赖
```bash

pip install -r requirements.txt
```

### 运行游戏
```bash
cd src
python main.py
```
## 训练机器学习模型
如果你想重新训练或改进AI的评估模型：

```bash
cd src/ml
python make_data.py   # 生成训练数据（需要较长时间）
python trainer.py     # 训练模型
```

## 运行AI对战评估
如果你想重新评估AI：
```bash
cd src/pk
python battle.py
```

## 评估结果
所有AI的对战结果保存在 `doc/pk/results/` 目录下。
最强两个AI的详细对战记录位于 `doc/pk/final_results/`。
