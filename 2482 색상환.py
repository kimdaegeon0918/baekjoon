# 색상환
# Gold 3, DP

MOD = 10**9+3

n,k = int(input()),int(input())

dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][1] = i
    dp[i][0] = 1

for i in range(2,n+1):
    for j in range(2,k+1):
        dp[i][j] = (dp[i-2][j-1]+dp[i-1][j])%MOD

print((dp[n-1][k]+dp[n-3][k-1])%MOD)