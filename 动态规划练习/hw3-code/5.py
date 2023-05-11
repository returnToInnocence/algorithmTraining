stick = []
choose = []

def match(count, num, index, target, lenth):
    '''
    count and target is the estimated number and lenth of final separation of all the sticks
    num and lenth are current separation, waiting for further check on whether they are valid
    index is whose sticks ready to be put in the same group, so that we can aviod those are already in the selected
    '''
    if num == count:
        return 1
    if lenth == target:
        return match(count, num + 1, 0, target, 0)
    for i in range(index, n):
        if choose[i] == 0:
            if stick[i] <= (target - lenth):
                choose[i] = 1
                if match(count, num, i + 1, target, lenth + stick[i]):
                    return 1
                else:
                    choose[i] = 0
                    if lenth == 0 or lenth+stick[i] == target:
                        return False
    return 0

while True:
    n = int(input())
    if n == 0:
        break
    stick = [int(x) for x in input().split(' ')]
    stick.sort()
    stick = stick[::-1]
    '''rearrange the stickes so that when we separate them'''
    choose = [0 for i in range(n)]
    '''mark the sorted stickes'''
    sumof = 0
    for i in stick:
        sumof += i
    for target in range(stick[0], sumof + 1):
        if sumof % target == 0:
            count = sumof / target
            if match(count, 0, 0, target, 0) == 1:
                print(target)
                break