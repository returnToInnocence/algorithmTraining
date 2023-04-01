n, Len, used, S, A = 0, 0, [], 0, []

def dfs(idx_last, cur, finished, totalNum):
    global n, Len, used, S, A
    """
    输入:
    idx_last: 上一根木棍的序号
    cur: 当前正在拼接木棒的长度（已经拼接了多长）
    finished: 已完成的木棒的个数
    输出: bool型, 是否拼接成功
    """
    # 记录失败的木棍长度
    lastA = None
    # 如果已完成的和猜测的结果一致，那么就返回
    if finished == totalNum:
        return True
    # 考虑当前木棒的第一根木棍, 必须是剩余木棍里面最长的那根.
    if cur == 0:
        # 一根根尝试
        for i in range(n):
            # 如果没被用过
            if not used[i]:
                # 更改这个位置的木棒为用过
                used[i] = True
                # 第一根木棍就填满了, 直接考虑下一个木棒
                if A[i] == Len:
                    tf = dfs(i, 0, finished + 1, totalNum)
                else:
                    tf = dfs(i, A[i], finished, totalNum)
                used[i] = False
                # 剪枝条件4: 第一根木棍失败, 那么方法肯定失败
                return tf
    else:
        # 考虑当前木棒的非第一根木棍
        for i in range(idx_last + 1, n):
            # 不再使用已经被使用的木棒
            if used[i]: continue
            # 剪枝条件3: 若一个木棍失败, 那么等长的其他木棍也肯定会失败
            if A[i] == lastA: continue
            # 如果一根木棒还原成功
            if cur + A[i] == Len:
                used[i] = True
                tf = dfs(i, 0, finished + 1, totalNum)
                # 剪枝条件5: 最后一根如果失败, 方案肯定失败
                used[i] = False
                return tf
            elif cur + A[i] < Len:
                used[i] = True
                tf = dfs(i, cur + A[i], finished, totalNum)
                used[i] = False
                # 如果没有拼接成功，那么就是说明这个棒子在拼接当前棒子的时候是不成功的（但是不代表参与后面的拼接不成功，这个和参与拼接的第一根棒子长度有关）
                if not tf:
                    lastA = A[i]
                else:
                    return True
    return False


def solve() -> int:
    global n, Len, used,S, A
    used = [False] * n
    # 降序排列，优化
    A.sort(reverse=True)
    # 所有木棒长度的总和
    S = sum(A)
    # 猜测木棒原长范围已经划定
    for Len in range(A[0], S + 1):
        # 如果不能被整除，那么就说明这个长度不能用 —— 优化
        if S % Len: continue
        totalNum = int(S / Len)
        if dfs(-1, 0, 0, totalNum):
            return Len


# %%
res = []
while True:
    n = int(input())
    if not n: break
    A = list(map(int, input().split()))
    res.append(solve())

for i in res:
    print(i)