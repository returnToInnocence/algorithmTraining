n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    w = input()
    for j in range(n):
        a[i][j] = int(w[j])


def change(i, j):
    if a[i][j] == 1:
        a[i][j] = 2
        if i != 0:
            change(i - 1, j)
        if i != n - 1:
            change(i + 1, j)
        if j != 0:
            change(i, j - 1)
        if j != n - 1:
            change(i, j + 1)


f = 0
for i in range(n):
    if f == 0:
        for j in range(n):
            if a[i][j] == 1:
                change(i, j)
                f = 1
                break
one = []
two = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            one.append([i, j])
        elif a[i][j] == 2:
            two.append([i, j])
far = []
for i in one:
    for j in two:
        far.append(abs(i[0] - j[0]) + abs(i[1] - j[1]))
print(min(far) - 1)
