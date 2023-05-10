def f(m, n):
    # 恒定只有一种划分，因为数就一个
    # 恒定1的划分，那就全一
    if n == 1 or m == 1:
        A[m][n] = 1
        return 1
    elif m == 0:
        A[m][n] = 1
        return 1
    elif n == 0:
        A[m][n] = 0
        return 0
    # 搜过了
    elif A[m][n] > 0:
        return A[m][n]
    else:
        # 没必要划分， 就赶紧变到可划分情况
        if m < n:
            A[m][n] = f(m, m)
        # 有一个包含相等情况，就一种划分，然后往下去找就好
        elif m == n:
            A[m][n] = 1 + f(m, n-1)
        elif m > n:
            A[m][n] = f(m, n - 1) + f(m - n, n)
    return A[m][n]

while True:
    try:
        m = int(input().strip())
        n = m
        A = [[0] * (n + 1) for i in range(m + 1)]
        print(f(m, n))
    except:
        break
