index = 0

def f():
    global index
    if index < len(s):
        index += 1
        if s[index-1] == '+':
            return f()+f()
        elif s[index-1] == '-':
            return f()-f()
        elif s[index-1] == '*':
            return f()*f()
        elif s[index-1] == '/':
            return f()/f()
        else:
            return float(s[index-1])


s = input().split(' ')
print("{:.6f}".format(f()))
