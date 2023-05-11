N=int(input())
lis=list(map(int,input().split()))
dp=[[0]*N for i in range(N)]
out=[]
for i in range(N):
    for j in range(i+1):
        if i==j:
            dp[i][j]=1
        elif lis[i]<=lis[j]:
            dp[i][j]=out[j]+1
    out.append(max(dp[i]))
print(max(out))