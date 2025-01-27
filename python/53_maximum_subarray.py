from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Function to return the sum of subarray with the largest sum

        Args:
            nums(List[int]): a list consist of integers

        Returns:
            int: the sum of subarray with the largest sum
        """
        # simple dp
        # Time: O(N)
        # Space: O(N)
        # N = len(nums)
        """
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)
        """
        # Time: O(N)
        # Space: O(1)
        # N = len(nums)
        i_max = res = nums[0]
        for i in range(1, len(nums)):
            i_max = max(i_max+nums[i], nums[i])
            res = max(res, i_max)
        return res
