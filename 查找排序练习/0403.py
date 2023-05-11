n, m = map(int, input().split())
a=[]
for i in range(n):
    a.append(int(input()))

l = a[0]
r = a[0]
for i in range(1, n):
    if a[i] > l:
        l = a[i]
    r += a[i]

while l < r:
    mid = (l + r) // 2
    s = a[0]
    c = 1
    for i in range(1, n):
        s += a[i]
        if s > mid:
            c += 1
            s = a[i]
    if c <= m:
        r = mid
    else:
        l = mid + 1

print(l)