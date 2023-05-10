text1 = input()
input()
text2 = input()
m, n = len(text1), len(text2)
dp = [[0 for y in range(n+1)] for i in range(m+1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if text1[i - 1] == text2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[m][n])