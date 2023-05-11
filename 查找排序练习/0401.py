l = [int(x) for x in input().split()]

a = []
b = []
for i in l:
    if i % 2 == 0:
        a.append(i)
    else:
        b.append(i)

a.sort()
b.sort(reverse=True)

l = b + a
print(' '.join([str(i) for i in l]))