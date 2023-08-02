class Solution:
    dp = [0] * 46
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    
    for i in range(4,46):
        dp[i] = dp[i - 1] + dp[i - 2]

    def climbStairs(self, n: int) -> int:
        return Solution.dp[n]