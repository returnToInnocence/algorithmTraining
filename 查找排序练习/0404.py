def mergesort(x, y):
    sum1 = 0
    kong = []
    if y - x > 1:
        mid = (x + y) // 2
        a = mergesort(x, mid)
        b = mergesort(mid, y)
        sum1 = a + b
        i = x
        j = mid
        k = x
        while i < mid and j < y:
            if lst[i] <= lst[j]:
                kong.append(lst[i])
                i += 1
            else:
                kong.append(lst[j])
                sum1 = sum1 + j - k
                j += 1
            k += 1
        while i < mid:
            kong.append(lst[i])
            k = k+1
            i = i+1
        while j < y:
            kong.append(lst[j])
            j = j + 1
            k = k + 1
        for t in range(x, y):
            lst[t] = kong[t - x]
    return sum1


n = int(input())
lst = list(map(int, input().split()))
lst = list(reversed(lst))
m = mergesort(0, len(lst))
print(m)
