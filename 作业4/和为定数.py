n = int(input())
num = list(map(int, input().split()))
m = int(input())
num.sort()
re = False
if m <= 2*num[n-1]:
    for i in range(n):
        tmp = m - num[i]
        if tmp in num:
            if tmp == num[i + 1] or tmp != num[i]:
                print(str(num[i]) + ' ' + str(m - num[i]), end='')
                re = True
                break
if not re:
    print('No')