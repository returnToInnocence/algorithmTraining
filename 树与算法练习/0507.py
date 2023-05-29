def DFS(tree, target):
    if len(tree) == 0:
        return False
    if tree[1] == [] and tree[2] == []:
        if tree[0] == target:
            return True
        else:
            return False
    res1 = False
    res2 = False
    if len(tree[1]):
        tree[1][0] += tree[0]
        res1 = DFS(tree[1], target)
    if len(tree[2]):
        tree[2][0] += tree[0]
        res2 = DFS(tree[2], target)
    return res1 or res2


while True:
    try:
        s = input()
    except:
        break

    s = s.replace("\n", "").split()
    target= int(s[0])
    tree = "".join(s[1:])
    tree = tree.replace('(', ',[')
    tree = tree.replace(')', ']')
    while True:
        try:
            tree = eval(tree[1:])
            break
        except:
            s = input()
            s = s.replace("\n", "").split()
            s = "".join(s)
            s = s.replace('(', ',[')
            s = s.replace(')', ']')
            tree += s

    if DFS(tree, target):
        print("yes")
    else:
        print("no")