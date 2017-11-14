def answer(n):
	dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
	dp[0][0] = 1
	for end in range(1, n+1):
	    for left in range(0, n+1):
	        dp[end][left] = dp[end-1][left]
	        if left >= end:
	            dp[end][left] += dp[end-1][left-end]
	return dp[n][n]-1
