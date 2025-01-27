from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dynamic programming
        # Time: O(N^2)
        # Space: O(N)
        # N = len(nums)
        """
        dp = [1]
        ans = 1
        for i in range(1, len(nums)):
            tmp = 1
        for j in range(i):
            if nums[j] < nums[i]:
                tmp = max(tmp, dp[j]+1)
        dp.append(tmp)
        ans = max(ans, tmp)
        return ans
        """
        # binary search
        # Time: O(NlogN)
        # Space: O(N)
        # N = len(nums)
        sub = []
        for num in nums:
            if len(sub) == 0 or sub[-1] < num:
                sub.append(num)
            else:
                idx = self.search(sub, num)
                sub[idx] = num
        return len(sub)

    def search(self, li, target):
        left, right = 0, len(li)
        while left != right:
            mid = (left+right) // 2
            if li[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
