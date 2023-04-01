# t是采药时间，m是山洞里草药数目
t, m = map(int, input().split())
# 种类作为行标，总时长（也就是限制条件作为列标），建立二维表
# value 这个草药要花费的时间
v = []
# weight 这个草药的价值
w = []
# 创建对应存储列表并初始化0，m行，t+1列，因为从1个开始，而不是0
f = [[0 for y in range(t+1)] for i in range(m)]
# 获取输入并分别存入对应list
for i in range(m):
    a,b = map(int, input().split())
    v.append(a)
    w.append(b)
# 草药数从0棵开始，（0，0）必定为 0，因为没有时间所以没法选草药
for i in range(0, m):
    for j in range(t+1):
        # 上一轮的最优解，-1的时候必定为0，因为还没放东西
        f[i][j] = f[i-1][j]
        # 如果现在背包里面还能放得下东西
        if j >= v[i]:
            # 考虑到底是放还是不放
            f[i][j] = max(f[i][j], f[i-1][j-v[i]]+ w[i])

print(f[m-1][t])
