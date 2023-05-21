import sys

index2 = 0
sum = 0
index = 0
class Node:
    def __init__(self):
        self.data = 0
        self.lchild = None
        self.rchild = None

def pre_order(s: str):
    pre_rst = []
    i = 0
    while i < len(s):
        if s[i] == '(':
            if s[i + 1] == ')':
                pre_rst.append(sys.maxsize)
            i += 1
            continue
        if s[i] == ')':
            i += 1
            continue

        # number
        ends = i
        while s[ends] == '-' or s[ends].isdigit():
            ends += 1
        substr = s[i:ends]
        num = int(substr)
        pre_rst.append(num)
        i = ends
    return pre_rst


def build_tree(pre_rst: list, root: Node):
    global index
    if index >= len(pre_rst):
        return
    num = pre_rst[index]
    if num == sys.maxsize:
        return
    else:
        root.data = num
        index += 1
        root.lchild = Node()
        build_tree(pre_rst,  root.lchild)
        index += 1
        root.rchild = Node()
        build_tree(pre_rst,  root.rchild)


def find_sum(root: Node, num: int):
    global ans, sum
    if root is None:
        return
    if (root.lchild is None) and (root.rchild is None):
        if sum + root.data == num:
            ans = 'yes'
        return
    sum += root.data
    find_sum(root.lchild, num)
    find_sum(root.rchild, num)
    sum -= root.data


def get_string2(tmpList) -> str:
    global index2
    l_count = 0
    r_count = 0
    s = ''
    while True:
        # c = sys.stdin.read(1)
        # print(tmpList[index2])
        c = tmpList[index2]
        index2 += 1
        if c.isdigit():
            s += c
            continue
        else:
            if c == ' ' or c == '\n' or c == '\t':
                continue
            if c == '(':
                l_count += 1
            if c == ')':
                r_count += 1
            s += c
            if l_count == r_count:
                break
    # print('有几行？')
    return s


getInput = ''
while True:
    tmp = input().replace(' ','')
    if len(tmp) == 0:
        break
    getInput += tmp

# print()
# print(getInput)
getInputLen = len(getInput)
inputLineList = []

while getInputLen != index2:
    inputLineList.append(get_string2(getInput))


for s in inputLineList:
    sIndex = 0

    N = ''
    while True:
        if s[sIndex].isdigit():
            # print(type(N))
            N += s[sIndex]
            sIndex += 1
        else:
            break
    N = int(N)
    s = s[sIndex:]
    pre_rst = pre_order(s)
    ptr = Node()
    index = 0
    build_tree(pre_rst, ptr)
    sum = 0
    ans = 'no'
    find_sum(ptr, N)
    print(ans)
