
def Count(N, L, R):

	dp = [[0 for i in range(R - L + 1)]
			for i in range(N)]

	ans = 0
	for i in range(N):
		dp[i][0] = 1

	for i in range(1, len(dp[0])):
		dp[0][i] = dp[0][i - 1] + 1

	ans = dp[0][R - L]

	for i in range(1, N):
		for j in range(1, len(dp[0])):
			dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
		ans += dp[i][R - L]
	return ans


n=int(input())
l=int(input())
r=int(input())

print(Count(n,l,r))