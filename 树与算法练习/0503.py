def dfs(pre, mid):
    if len(pre) <= 1:
        return pre

    root = pre[0]
    left_mid = mid[:mid.index(root)]
    len_left = len(left_mid)
    right_mid = mid[mid.index(root) + 1:]

    left_pre = pre[1:1 + len_left]
    right_pre = pre[1 + len_left:]

    return dfs(left_pre, left_mid) + dfs(right_pre, right_mid) + root


while True:
    try:
        p, m = input().split()
        print(dfs(p, m))

    except EOFError:
        break
