from core.constants import *


def within_board(row, col):
    return (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE)

def debug(board):
    """打印棋盘状态"""
    symbols = {BLACK: '●', WHITE: '○', EMPTY: '·'}
    print("  ", end="")
    for col in range(BOARD_SIZE):
        print(f"{col:2d}", end="")
    print()
    for row in range(BOARD_SIZE):
        print(f"{row:2d} ", end="")
        for col in range(BOARD_SIZE):
            print(symbols[board.board[row][col]], end=" ")
        print()
    print("features",board.features)


def evaluate(board):

    score = 0
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    # 位置权重表 - 中心位置价值更高
    center_weights = [[min(i, j, BOARD_SIZE - 1 - i, BOARD_SIZE - 1 - j) + 1 for j in range(BOARD_SIZE)] for i in
                      range(BOARD_SIZE)]

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            color = board.board[i][j]
            if color == EMPTY:
                continue

            # 位置价值
            pos_value = center_weights[i][j]
            score += pos_value if color == WHITE else -pos_value

            # 四个方向的棋型评估
            for dr, dc in directions:
                # 避免重复计算
                if within_board(i - dr, j - dc) and board.board[i - dr][j - dc] == color:
                    continue

                # 评估这个方向的连续和间隔棋型
                direction_score = evaluate_direction(board, i, j, dr, dc, color)
                score += direction_score if color == WHITE else -direction_score
    # debug(board)
    # print("score = ",score)
    return score


def evaluate_direction(board, row, col, dr, dc, color):
    """评估一个方向上的所有棋型"""
    score = 0

    # 连续棋型评估
    continuous_score = evaluate_continuous(board, row, col, dr, dc, color)
    score += continuous_score

    # 间隔棋型评估
    gap_score = evaluate_gap_patterns(board, row, col, dr, dc, color)
    score += gap_score

    return score


def evaluate_continuous(board, row, col, dr, dc, color):
    """评估连续棋型"""
    count = 0
    r, c = row, col

    # 统计连续数量
    while within_board(r, c) and board.board[r][c] == color:
        count += 1
        r += dr
        c += dc

    # 检查两端阻塞
    start_blocked = not within_board(row - dr, col - dc) or board.board[row - dr][col - dc] == opponent(color)
    end_blocked = not within_board(r, c) or board.board[r][c] == opponent(color)
    block_count = start_blocked + end_blocked

    # 连续棋型价值表
    values = {
        5: 100000,  # 五连
        4: {0: 10000, 1: 1000, 2: 100},  # 活四、冲四、死四
        3: {0: 5000, 1: 500, 2: 50},  # 活三、眠三、死三
        2: {0: 200, 1: 20, 2: 2},  # 活二、眠二、死二
        1: {0: 1, 1: 0, 2: 0}  # 单子
    }

    if count >= 5:
        return values[5]
    elif count in values:
        return values[count].get(block_count, 0)
    return 0


def evaluate_gap_patterns(board, row, col, dr, dc, color):
    """评估间隔棋型"""
    score = 0

    # 检查三子和四子的间隔模式
    gap_patterns = [
        # 三子间隔模式 (跳三)
        [[0, 1, 3], 800],  # ○_○○ 活跳三
        [[0, 2, 3], 800],  # ○○_○ 另一种跳三

        # 四子间隔模式 (跳四)
        [[0, 1, 2, 4], 5000],  # ○_○○○ 跳四
        [[0, 1, 3, 4], 5000],  # ○○_○○ 跳四
        [[0, 2, 3, 4], 5000],  # ○_○○○ 另一种跳四
    ]

    for pattern, value in gap_patterns:
        if check_pattern(board, row, col, dr, dc, color, pattern):
            score += value

    return score


def check_pattern(board, row, col, dr, dc, color, pattern):
    """检查特定模式是否存在"""
    max_offset = max(pattern)

    # 检查模式中的所有位置
    for offset in pattern:
        r, c = row + dr * offset, col + dc * offset
        if not within_board(r, c) or board.board[r][c] != color:
            return False

    # 检查间隔位置是否为空（确保是间隔模式）
    for offset in range(max_offset + 1):
        if offset not in pattern:  # 这个位置应该是间隔
            r, c = row + dr * offset, col + dc * offset
            if within_board(r, c) and board.board[r][c] != EMPTY:
                return False

    return True


def opponent(color):
    """返回对手颜色"""
    return BLACK if color == WHITE else WHITE