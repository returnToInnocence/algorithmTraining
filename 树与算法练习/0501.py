ans = 0
s = input().split()
stack = []

for c in s:
    if c in ['*', '+', '/', '-']:
        # print("1___"+c)
        stack.append(c)
    else:
        # print("2"+c)
        stack.append(float(c))
        # 这里是需要思考的点
        # 3个才存在计算的余地
        #
        while len(stack) > 2 and stack[-2] not in ['*', '+', '/', '-']:
            # b = 0
            b = stack.pop()
            # print(b)
            a = stack.pop()
            # print(a)
            x = stack.pop()
            # print(x)
            if x == '*':
                stack.append(a * b)
            elif x == '+':
                stack.append(a + b)
            elif x == '-':
                stack.append(a - b)
            else:
                stack.append(a / b)


print('%.6f' % stack.pop())
