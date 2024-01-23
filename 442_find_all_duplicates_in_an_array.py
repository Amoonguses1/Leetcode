# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            num = abs(num)
            if nums[num-1] < 0:
                ans.append(num)
            else:
                nums[num-1] = -nums[num-1]
        return ans
