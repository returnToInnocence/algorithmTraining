r,c = map(int,input().split())
numlist =[]
for i in range(r):
    numlist.append(list(map(int,input().split())))
dpcount = [[0 for i in range(c)]for j in range(r)]
def LoogestPath(i,j):
    if dpcount[i][j] != 0:
        return dpcount[i][j]
    for k in range(4):
        x1 = i+dx[k]
        y1 = j+dy[k]
        if 0 <= x1 < r and 0 <= y1 < c and numlist[x1][y1] < numlist[i][j]:
            dpcount[i][j] = max(dpcount[i][j], LoogestPath(x1, y1)+1)
    return dpcount[i][j]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dp = 0
for i in range(r):
    for j in range(c):
        dp = max(dp,LoogestPath(i,j))

print(dp+1)