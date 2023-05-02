n, m = map(int, input().split())
expenditure = []
for _ in range(n):
    expenditure.append(int(input()))


def check(x):
    num, s = 1, 0
    for i in range(n):
        if s + expenditure[i] > x:
            s = expenditure[i]
            num += 1
        else:
            s += expenditure[i]
    return [False, True][num > m]


lo = max(expenditure)
hi = sum(expenditure)
while lo < hi:
    mid = (lo + hi) // 2
    if check(mid):
        lo = mid + 1
    else:
        hi = mid
print(lo)
