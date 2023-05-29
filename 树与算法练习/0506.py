n = int(input())
nodes = input().split()
lines = [nodes[0][0]]
index = [0]
unfilled = [0]
for i in range(1, n):
    if nodes[i - 1][1] == '0':
        index.append(index[-1] + 1)
    else:
        index.append(index[unfilled.pop()])
    if nodes[i][1] == '0':
        unfilled.append(i)
    if nodes[i][0] != '$':
        if index[-1] >= len(lines):
            lines.append(nodes[i][0])
        else:
            lines[index[-1]] = nodes[i][0] + ' ' + lines[index[-1]]
print(' '.join(lines))
