a = input()
pre, pos = 0, 0
dpre, dpos = 0, 0

node = len(a) // 2
for i in a:
    if i == "d":
        dpre += 1
    elif i == "u":
        dpre -= 1
    pre = max(pre, dpre)
t = []
for j in range(len(a) - 1):
    if a[j] == "d":
        dpos += 1
        if a[j + 1] == "d":
            t.append(dpos)
    elif a[j] == "u":
        dpos -= 1
        if a[j + 1] == "u":
            dpos = t.pop()
        elif a[j + 1] == "d":
            dpos += 1
    pos = max(dpos, pos)
print(pre, "=>", pos)
