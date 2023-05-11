s = input()
length = len(s)
dp  = [[-1]*length for i in range(length)]
def func(l,r):
    if l>=r:
        dp[l][r]=0
        return 0 
    if dp[l][r]!=-1:
        return dp[l][r]
    if s[l]==s[r]:
        dp[l][r] = func(l+1,r-1)
        return dp[l][r]
    else:
        dp[l][r] =1+ min(func(l+1,r),func(l,r-1),func(l+1,r-1))
        return dp[l][r]
print(func(0,length-1))