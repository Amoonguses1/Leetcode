# Time: O(MNlogN)
# Space: O(N+M)
# M = len(lefts) = len(r)
# N = len(nums)
from typing import List


class Solution:
    def checkArithmeticSubarrays(
            self,
            nums: List[int],
            lefts: List[int],
            rights: List[int]
    ) -> List[bool]:
        res = []
        for i in range(len(lefts)):
            arr = nums[lefts[i]:rights[i]+1]
            res.append(self.isArithmetic(arr))
        return res

    def isArithmetic(self, nums: List[int]) -> bool:
        nums.sort()
        diff = nums[1] - nums[0]
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] != diff:
                return False
        return True
