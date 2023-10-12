class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:

        dp = [[[None] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        return self.dfs(n, m, k, 0, 0, 0, dp)

    def dfs(self, n, m, k, i, curMax, curCost, dp):
        if i == n:
            if k == curCost:
                return 1
            return 0

        if dp[i][curMax][curCost] is not None:
            return dp[i][curMax][curCost]

        ans = 0
        for num in range(1, m + 1):
            newCost = curCost
            newMax = curMax
            if num > curMax:
                newMax = num
                newCost += 1
            if newCost > k:
                break
            
            ans += self.dfs(n, m, k, i + 1, newMax, newCost, dp)
            ans %= 1000000007

        dp[i][curMax][curCost] = ans
        return ans
    
    


    