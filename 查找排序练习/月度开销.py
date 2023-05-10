n, m = map(int, input().split())
expenses = []
for i in range(n):
    expenses.append(int(input()))

left, right = max(expenses), sum(expenses)

while left < right:
    mid = (left + right) // 2
    
    # 判断是否存在一个方案使得最大月度开销不超过mid
    count = 1
    cur_sum = 0
    for expense in expenses:
        if cur_sum + expense > mid:
            count += 1
            cur_sum = expense
        else:
            cur_sum += expense
    if count <= m:
        right = mid
    else:
        left = mid + 1

print(left)