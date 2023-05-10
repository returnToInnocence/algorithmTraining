from collections import deque


class Solution:
    def shortestBridge(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        points = deque()

        # dfs寻找第一个岛屿,并把1赋值为2,并把其周边的海洋入队
        def dfs(points, grid, m, n, i, j):
            if i < 0 or i == m or j < 0 or j == n or grid[i][j] == 2:
                return
            if grid[i][j] == 0:
                points.append((i, j))
                return

            grid[i][j] = 2
            dfs(points, grid, m, n, i - 1, j)
            dfs(points, grid, m, n, i + 1, j)
            dfs(points, grid, m, n, i, j - 1)
            dfs(points, grid, m, n, i, j + 1)

        # bfs寻找第二个岛屿,并把过程中经过的0赋值给2
        flag = False
        for i in range(m):
            if flag:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(points, grid, m, n, i, j)
                    flag = True
                    break

        x, y, count = 0, 0, 0
        while points:
            count += 1
            n_points = len(points)
            while n_points > 0:
                point = points.popleft()
                r, c = point[0], point[1]
                for k in range(4):
                    x, y = r + direction[k], c + direction[k + 1]
                    if x >= 0 and y >= 0 and x < m and y < n:
                        if grid[x][y] == 2:
                            continue
                        if grid[x][y] == 1:
                            return count
                        points.append((x, y))
                        grid[x][y] = 2
                n_points -= 1

        return 0


direction = [-1, 0, 1, 0, -1]

n = int(input())
grid = []
for i in range(n):
    row = list(map(int, list(input())))
    grid.append(row)

print(Solution().shortestBridge(grid))