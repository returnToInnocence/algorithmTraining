ans = 0
s = input().split()
stack = []

for c in s:
    if c in ['*', '+', '/', '-']:
        stack.append(c)
    else:
        stack.append(float(c))
        while len(stack) > 2 and stack[-2] not in ['*', '+', '/', '-']:
            b = stack.pop()
            a = stack.pop()
            x = stack.pop()
            if x == '*':
                stack.append(a * b)
            elif x == '+':
                stack.append(a + b)
            elif x == '-':
                stack.append(a - b)
            else:
                stack.append(a / b)

print('%.6f' % stack.pop())
