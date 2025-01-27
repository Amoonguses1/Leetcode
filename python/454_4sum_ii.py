# Time: O(N^2)
# Space: O(N^2)
# N = len(nums1)
from typing import List
from collections import defaultdict


class Solution:
    def fourSumCount(
        self,
        nums1: List[int],
        nums2: List[int],
        nums3: List[int],
        nums4: List[int]
    ) -> int:
        ans, sumDict = 0, defaultdict(int)
        for num1 in nums1:
            for num2 in nums2:
                sumDict[num1+num2] += 1
        for num3 in nums3:
            for num4 in nums4:
                ans += sumDict[0-(num3+num4)]
        return ans
