import heapq

for _ in range(int(input())):
    m, n = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort()
    min_sum = [x for x in a]
    for i in range(m - 1):
        b = [int(x) for x in input().split()]
        b.sort()

        temp = [-b[0] - j for j in min_sum]
        heapq.heapify(temp)
        for j in range(n):
            for k in range(1, n):
                if min_sum[j] + b[k] < -temp[0]:
                    heapq.heapreplace(temp, -min_sum[j] - b[k])
                    heapq.heapify(temp)
                else:
                    break
        min_sum = [-x for x in temp]
        min_sum.sort()

    print(' '.join([str(x) for x in min_sum]))
