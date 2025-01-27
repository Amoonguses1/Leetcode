from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # iterative dp
        # Time: O(N*target)
        # Space: O(target)
        # N = len(nums)
        """
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i-num]
        return dp[target]
        """
        # recursive dp
        # Time: O(N*target)
        # Space: O(target)
        # N = len(nums)
        self.dp = [-1] * (target+1)
        return self.countCombinations(nums, target)

    def countCombinations(self, nums, target):
        if target < 0:
            return 0

        if target == 0:
            return 1

        if self.dp[target] != -1:
            return self.dp[target]

        cur_combinations = 0
        for cur in nums:
            cur_combinations += self.countCombinations(nums, target-cur)
        self.dp[target] = cur_combinations
        return cur_combinations
