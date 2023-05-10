inputStr = input()
strLen = len(inputStr)
dp = [[0 for y in range(strLen+1)] for i in range(strLen+1)]

for i in range(strLen-1, -1, -1):
    for j in range(i, strLen):
        if inputStr[i] == inputStr[j]:
            dp[i][j] = dp[i+1][j-1]
        else:
            dp[i][j] = min(dp[i+1][j],dp[i][j-1],dp[i+1][j-1]) + 1
print(dp[0][strLen-1])
