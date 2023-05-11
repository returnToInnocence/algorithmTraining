myTime,numHerb=map(int,input().split())
herbList=[]
for i in range(numHerb):
    charm=list(map(int,input().split()))
    herbList.append(charm)

dp=[[0]*(myTime+1) for i in range(numHerb+1)]
for i in range(1,numHerb+1):
    for j in range(1,myTime+1):
        if herbList[i-1][0]<=j:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-herbList[i-1][0]]+herbList[i-1][1])
        else:
            dp[i][j]=dp[i-1][j]

print(dp[numHerb][myTime])