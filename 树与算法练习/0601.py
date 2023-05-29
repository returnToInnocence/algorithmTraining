m, n = list(map(int, input().split()))
while m != n:
    if m > n:
        m = m // 2
    elif m < n:
        n = n // 2

print(m)
