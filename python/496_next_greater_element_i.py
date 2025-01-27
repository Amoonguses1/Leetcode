# Time: O(N+M)
# Space: O(N+M)
# N = len(nums1), M = len(nums2)
from typing import List


class Solution:
    def nextGreaterElement(
        self, nums1: List[int], nums2: List[int]
    ) -> List[int]:
        nxtGreater = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                cur = stack.pop()
                nxtGreater[cur] = num
            stack.append(num)
        return [nxtGreater.get(num, -1) for num in nums1]
