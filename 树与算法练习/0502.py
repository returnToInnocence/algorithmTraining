while True:
    m, n = [int(x) for x in input().split()]
    if m == 0 and n == 0:
        break

    ans = 1
    ls = 1
    left, right = 2 * m, 2 * m + 1

    while n >= right:
        ls *= 2
        ans += ls
        left, right = 2 * left, 2 * right + 1

    ans += max(0, n - left + 1)
    print(ans)
