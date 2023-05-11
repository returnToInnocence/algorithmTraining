L = []

n = int(input())
for i in range(n):
    a, b, c = input().split()
    a = [int(x) for x in a.split('.')]
    b = [int(x) for x in b.split('.')]
    L.append([(b[0]-1)*31 + b[1] - 7,
              (a[0]-1)*31 + a[1] - 7,
              int(c)])
L.sort()
ans = [0 for _ in range(46)]
for i in range(L[0][0], 45):
    ans[i + 1] = L[0][2]
for s in range(1, n):
    if L[s][0] >= 45:
        continue
    t = max(ans[L[s][0]+1], ans[L[s][1]]+L[s][2])
    for i in range(L[s][0], 45):
        ans[i + 1] = t
print(ans[-1])
