n = int(input())
depth = [0] * (n + 1)
depth[1] = 1

for i in range(1, n + 1):
    left, right = [int(x) for x in input().split()]
    if left > 0:
        depth[left] = depth[i] + 1
    if right > 0:
        depth[right] = depth[i] + 1

print(max(depth))
