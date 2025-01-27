from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """Function to find the minimum number of jumps to reach nums[n-1]

        Args:
            nums(List[int]): nums[i] represents the maximum length of
                a forward jump from index i

        Returns:
            int: the minimum number of jumps
        """
        # simple dp
        # Time: O(N**2)
        # Space: O(N)
        """
        n = len(nums)
        dp = [n] * n
        dp[0] = 0
        for i in range(n):
            for j in range(1, nums[i]+1):
                if i + j >= n:
                    break
                dp[i+j] = min(dp[i+j], dp[i]+1)
        return dp[n-1]
        """
        # Time: O(N)
        # Space: O(1)
        n = len(nums)
        start, end, step = 0, 0, 0
        while end < n - 1:
            step += 1
            extend = end + 1
            for i in range(start, end+1):
                if i + nums[i] >= n:
                    return step

                extend = max(extend, i+nums[i])
            start, end = end + 1, extend
        return step
