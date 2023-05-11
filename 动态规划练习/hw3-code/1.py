def f(m,n):
    if m<=0:
        return 0
    elif n==1 or m==0:    
        return 1
    else:
        return(f(m-1,n-1)+f(m-n,n))
while True:

    try:    
        N=int(input())
        print(sum([f(N,i) for i in range(1,N+1)]))
    except EOFError:
        break