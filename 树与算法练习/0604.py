l = []
r = []
alist = list(map(int, input().split()))


def insert(p, i):
    if alist[i] == alist[p]:
        return
    if alist[i] < alist[p]:
        if l[p] == -1:
            l[p] = i
            return
        else:
            insert(l[p], i)
    else:
        if r[p] == -1:
            r[p] = i
            return
        else:
            insert(r[p], i)


def preorder(p):
    if p < 0:
        return
    print(alist[p], end=' ')
    preorder(l[p])
    preorder(r[p])


n = len(alist)
for e in range(n):
    l.append(-1)
    r.append(-1)
    if e > 0:
        insert(0, e)
preorder(0)
