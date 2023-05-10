n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] = -a[i]

cnt = 0
temp = [0] * n

def merge(left, right, mid):
    global cnt
    index1, index2 = left, mid+1
    for i in range(left, right+1):
        temp[i] = a[i]
    s = left
    while index1 <= mid and index2 <= right:
        if temp[index1] <= temp[index2]:
            a[s] = temp[index1]
            s += 1
            index1 += 1
        else:
            cnt += (mid - index1 + 1)
            a[s] = temp[index2]
            s += 1
            index2 += 1
    while index1 <= mid:
        a[s] = temp[index1]
        s += 1
        index1 += 1
    while index2 <= right:
        a[s] = temp[index2]
        s += 1
        index2 += 1

def mymerge(left, right):
    if left < right:
        mid = (left + right) // 2
        mymerge(left, mid)
        mymerge(mid + 1, right)
        merge(left, right, mid)

mymerge(0, n-1)
print(cnt)