from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Time: O(N)
        # Space: O(N)
        # N = len(nums)
        # hash table solution
        count = Counter(nums)
        ans = 0
        for key in count:
            if key+1 in count:
                ans = max(ans, count[key]+count[key+1])
        return ans

    def findLHS2(self, nums: List[int]) -> int:
        # Time: O(NlogN)
        # Space: O(N)
        # N = len(nums)
        # sort solution
        nums.sort()
        indices = [0]
        prev = nums[0]
        for i, num in enumerate(nums):
            if num != prev:
                prev = num
                indices.append(i)
        if len(indices) < 2:
            return 0

        if len(indices) == 2:
            if nums[-1] - nums[0] == 1:
                return len(nums)
            else:
                return 0

        ans = 0
        for i in range(len(indices)-2):
            if nums[indices[i+1]] - nums[indices[i]] == 1:
                ans = max(ans, indices[i+2]-indices[i])
        if nums[-1] - nums[indices[-2]] == 1:
            ans = max(ans, len(nums) - indices[-2])
        return ans
