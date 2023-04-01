import collections
from typing import List


# 当前位置的上下左右位置计算方式
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def longestIncreasingPath(matrix: List[List[int]]) -> int:
    # 确定输入正常
    if not matrix:
        return 0

    # 行列长度
    rows, columns = len(matrix), len(matrix[0])
    # 初始化二维列表
    outdegrees = [[0] * columns for i in range(rows)]
    # 队列的库
    queue = collections.deque()

    # 本质上目的是为了找到度为0的值
    for i in range(rows):
        for j in range(columns):
            # 上下左右四个方位计算
            for dx, dy in DIRS:
                newRow, newColumn = i + dx, j + dy
                # 先验证范围，防止list越界
                if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[i][j]:
                    outdegrees[i][j] += 1
            # 上下左右都扫完，没有可以走的，那么就是最大的位置
            if outdegrees[i][j] == 0:
                # 队列中存的是一个元组，表示度为0
                queue.append((i, j))

    ans = 0
    while queue:
        # 就是深度
        ans += 1
        size = len(queue)
        # 把queue中的元素全部拿出来挨个去尝试
        for i in range(size):
            row, column = queue.popleft()
            for dx, dy in DIRS:
                newRow, newColumn = row + dx, column + dy
                if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] < matrix[row][
                    column]:
                    # 度减一，进入下一层
                    outdegrees[newRow][newColumn] -= 1
                    # 为零，就参与下一轮搜索
                    if outdegrees[newRow][newColumn] == 0:
                        queue.append((newRow, newColumn))

    return ans


row, colum = map(int, input().split())
f = []
for i in range(row):
    f.append(list(map(int, input().split())))
print(longestIncreasingPath(f))

