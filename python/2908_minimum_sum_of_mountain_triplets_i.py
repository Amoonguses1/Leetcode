
from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        # Time: O(N)
        # Space: O(N)
        # N = len(nums)
        prefix = [float("inf")]
        suffix = [float("inf")]
        for i in range(len(nums)):
            if nums[i] < prefix[-1]:
                prefix.append(nums[i])
            else:
                prefix.append(prefix[-1])
            if nums[len(nums)-i-1] < suffix[-1]:
                suffix.append(nums[len(nums)-i-1])
            else:
                suffix.append(suffix[-1])

        ans = float("inf")
        for i, num in enumerate(nums):
            cur = num + prefix[i] + suffix[-i-1]
            if num > prefix[i] and num > suffix[-i-1]:
                ans = min(ans, cur)
        return ans if ans != float("inf") else -1

    def minimumSum2(self, nums: List[int]) -> int:
        # Time: O(N^2)
        # Space: O(1)
        # N = len(nums)
        ans = float("inf")
        for i in range(1, len(nums)-1):
            prefix = min(nums[:i])
            suffix = min(nums[i+1:])
            if nums[i] > prefix and nums[i] > suffix:
                ans = min(ans, prefix+nums[i]+suffix)
        return ans if ans != float('inf') else -1
