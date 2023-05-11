n = int(input())
s = [int(x) for x in input().split()]
m = int(input())

s.sort()

def search(l, r, target):
    if l > r:
        return False
    mid = int((l + r) / 2)
    if s[mid] == target:
        return True
    elif s[mid] > target:
        return search(l, mid - 1, target)
    else:
        return search(mid + 1, r, target)


for i in range(n):
    if s[i] > m / 2:
        print('No')
        break
    elif s[i] == m / 2 and s.count(s[i]) > 1:
        print(s[i], s[i])
        break
    elif s[i] < m / 2:
        if search(0, n - 1, m - s[i]):
            print(s[i], m - s[i])
            break
    if i == n - 1:
        print('No')