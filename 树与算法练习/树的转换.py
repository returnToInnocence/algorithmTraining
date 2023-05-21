import math

cnt = 0

t = input()
nh, h, nh2, h2 = 0, 0, 0, 0
now = [0]
for c in t:
    if c == "d":
        nh += 1
        nh2 += 1
        now.append(nh2)
    else:
        nh -= 1
        nh2 = now[-1]
        now.pop()
    h2 = max(h2, nh2)
    h = max(h, nh)
cnt += 1
print("%d => %d" % (h, h2))
