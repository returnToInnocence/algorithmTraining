s=input()
n=len(s)

dp=[[0]*(n+1) for i in range(n+1)]

for _ in range(n):
    dp[_][_]=0
    
for j in range(n):
    for i in range(j,-1,-1):
        if s[i]==s[j]:
            dp[i][j]=dp[i+1][j-1]
        else:
            dp[i][j]=min(dp[i][j-1]+1, dp[i+1][j]+1, dp[i+1][j-1]+1)
            
print(dp[0][n-1])