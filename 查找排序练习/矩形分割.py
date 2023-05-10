R = int(input())
N = int(input())

L, T, W, H = [0] * (N+1), [0] * (N+1), [0] * (N+1), [0] * (N+1)
for i in range(1, N+1):
    L[i], T[i], W[i], H[i] = map(int, input().split())

def S(k):
    # 计算左边减右边矩形面积
    sz, sy = 0, 0
    for i in range(1, N+1):
        # 全在左边
        if L[i] + W[i] <= k:
            sz += W[i] * H[i]
        # 全在右边
        elif L[i] >= k:
            sy += W[i] * H[i]
        # 左右都有
        else:
            sz += (k - L[i]) * H[i]
            sy += (L[i] + W[i] - k) * H[i]
    # 返回左边减右边的值
    return sz - sy

j, m = 0, R
while j < m:
    mid = (j + m) // 2
    if S(mid) >= 0:
        m = mid
    else:
        j = mid + 1

while j + 1 <= R and S(j) == S(j+1):
    j += 1
print(j)