from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Time: O(N * sum)
        # Space: O(N * sum)
        # N = len(nums), sum = sum(nums)
        # dp solution
        """
        total = sum(nums)
        if target > total or target < -1 * total:
            return 0

        dp = [[0 for _ in range(total*2+1)]for _ in range(len(nums))]

        dp[0][total + nums[0]] += 1
        dp[0][total - nums[0]] += 1
        for i in range(1, len(nums)):
            for j in range(total*2 + 1):
                if j - nums[i] >= 0 :
                    dp[i][j] += dp[i-1][j-nums[i]]

                if j + nums[i] <= total *2:
                    dp[i][j] += dp[i-1][j+nums[i]]

        return dp[-1][total+target]
        """
        # Time: O(N * sum)
        # Space: O(N * sum)
        # N = len(nums), sum = sum(nums)
        # dfs solution
        return self.dfs(target, nums, {})

    def dfs(self, cur, nums, memo):
        key = (cur, tuple(nums))
        if key in memo:
            return memo[key]

        if not nums:
            return 1 if cur == 0 else 0

        res = 0
        res += self.dfs(cur-nums[0], nums[1:], memo)
        res += self.dfs(cur+nums[0], nums[1:], memo)
        memo[key] = res
        return res
