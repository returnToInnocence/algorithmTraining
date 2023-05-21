from queue import PriorityQueue

q = PriorityQueue()

n = int(input())
a = list(map(int, input().split()))

for i in range(len(a)):
    q.put(a[i], a[i])

sum_num = 0
while q.qsize() > 1:
    a = q.get()
    b = q.get()
    q.put(a+b)
    sum_num += a+b

print(sum_num)