import queue

class TreeNode:
    def __init__(self, x):
        self.x = x
        self.lchild = None
        self.rchild = None

tree = [TreeNode('') for i in range(0,1002)]
loc = 0
index = 0

def create():
    global loc
    # 生成一个新的结点，并将其孩子结点置为 None
    tree[loc].lchild = None
    tree[loc].rchild = None
    loc += 1
    return tree[loc-1]

def build(temp):
    # 该题输入为伪满二叉树的前序遍历，利用 0、1 标志来识别外结点和内结点
    global index, tempList
    index += 1
    p = create()
    p.x = temp[0]
    if temp[1] == '0' and p.x != '$':
        # 因为已经给出 01 标志了，并且是伪满二叉树，所以这道题目的 n(树的结点个数) 信息冗余
        p.lchild = build(tempList[index])
        p.rchild = build(tempList[index])
    return p

def Print(p):
    # 输出该树的镜像翻转
    s = []
    Q = queue.Queue()
    # 此处是关键，根据“左孩子右兄弟”的特点，一直向右遍历，将树同一层的结点都放在栈内
    while p is not None:
        if p.x != '$':
            s.append(p)
        p = p.rchild
    # 将栈内的结点依次弹出，压入队列，完成镜像翻转的功能
    while len(s) > 0:
        Q.put(s[-1])
        del s[-1]
    while not Q.empty():
        p = Q.get()
        print(p.x, end=' ')
        if p.lchild is not None:
            p = p.lchild
            # 同理，上面是处理根节点的，因为那时队列还为空，这里是处理剩下的全部结点
            while p is not None:
                if p.x != '$':
                    s.append(p)
                p = p.rchild
            while len(s) > 0:
                Q.put(s[-1])
                del s[-1]


n = int(input())
tempList = input().split(' ')

root = build(tempList[index])
Print(root)
