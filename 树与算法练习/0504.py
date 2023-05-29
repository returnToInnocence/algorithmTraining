import heapq

n = int(input())
l = [int(x) for x in input().split()]

heapq.heapify(l)
ans = 0

while len(l) > 1:
    a = heapq.heappop(l)
    b = heapq.heappop(l)
    ans = ans + a + b
    heapq.heappush(l, a + b)

print(ans)
