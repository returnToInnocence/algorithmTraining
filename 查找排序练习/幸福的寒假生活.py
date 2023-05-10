f = [0] * 105
from_list = [[] for _ in range(105)]
n = int(input())
for i in range(1, n+1):
    st, ed, val = input().split()
    val = int(val)
    st_m = int(st[0])
    st_d = int(st[2])
    if len(st) == 4:
        st_d = st_d*10+int(st[3])
    ed_m = int(ed[0])
    ed_d = int(ed[2])
    if len(ed) == 4:
        ed_d = ed_d*10+int(ed[3])
    d1 = st_d
    if st_m == 2:
        d1 += 31
    d2 = ed_d
    if ed_m == 2:
        d2 += 31
    if d1 >= 7 and d2 <= 51:
        from_list[d2].append((d1, val))

ans = 0
for i in range(1, 101):
    f[i] = max(f[i], f[i-1])
    for it in from_list[i]:
        f[i] = max(f[i], f[it[0]-1]+it[1])
        ans = max(ans, f[i])

print(ans)