def cal(i, a, b):
    if i == '+':
        return a + b
    elif i == '-':
        return a - b
    elif i == '*':
        return a * b
    elif i == '/':
        return a // b


exp = input()
n = int(input())
value = {}
for _ in range(n):
    inf = input().split()
    value[inf[0]] = int(inf[1])
op = []
num = []
val = []
prior = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
for i in exp:
    if i == '(':
        op.append(i)
    elif i in '+-*/':
        while op and prior[i] <= prior[op[-1]]:
            n2 = num.pop()
            v2 = val.pop()
            n1 = num.pop()
            v1 = val.pop()
            ope = op.pop()
            num.append('(' + n1 + ope + n2 + ')')
            val.append(cal(ope, v1, v2))
        op.append(i)
    elif i == ')':
        while op[-1] != '(':
            n2 = num.pop()
            v2 = val.pop()
            n1 = num.pop()
            v1 = val.pop()
            ope = op.pop()
            num.append('(' + n1 + ope + n2 + ')')
            val.append(cal(ope, v1, v2))
        ope = op.pop()
    else:
        num.append(i)
        val.append(value[i])
while op:
    n2 = num.pop()
    v2 = val.pop()
    n1 = num.pop()
    v1 = val.pop()
    ope = op.pop()
    num.append('(' + n1 + ope + n2 + ')')
    val.append(cal(ope, v1, v2))
exp = num[0]

tree = []
cur = tree
path = [cur]
depth = 1
m = 1
for i in exp:
    if i == '(':
        cur.extend([0, [], []])
        cur = cur[1]
        path.append(cur)
        depth += 1
        m = max(m, depth)
    elif i == ')':
        temp  =path.pop()
        depth -= 1
        if path:
            cur = path[-1]
    elif i in '+-*/':
        cur[0] = i
        cur = cur[2]
        path.append(cur)
        depth += 1
        m = max(m, depth)
    else:
        cur.extend([i, [], []])
        temp = path.pop()
        depth -= 1
        cur = path[-1]


def rear(tree):
    if tree[1] and tree[2]:
        return rear(tree[1]) + rear(tree[2]) + tree[0]
    else:
        return tree[0]


print(rear(tree))
mat=[[' ' for i in range(2 ** m - 1)] for j in range(2 * m - 1)]


def write(tree, i, j):
    mat[i][j]=tree[0]
    if tree[1] and tree[2]:
        mat[i + 1][j - 1] = '/'
        mat[i + 1][j + 1] = '\\'
        write(tree[1], i + 2, j - 2 ** (m - 2 - i // 2))
        write(tree[2], i + 2, j + 2 ** (m - 2 - i // 2))


write(tree, 0, 2 ** (m - 1) - 1)
for i in mat:
    print(''.join(map(str, i)).rstrip())
print(val[0])
