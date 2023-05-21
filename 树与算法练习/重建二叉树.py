xb = 0

def work(l, r):
    global xb
    if l > r:
        return
    a = q[xb]
    xb += 1
    i = z.index(a)
    work(l, i-1)
    work(i+1, r)
    print(a, end='')

while True:
    try:
        q, z = input().split()
    except:
        break
    xb = 0
    work(0, len(z)-1)
    print()

