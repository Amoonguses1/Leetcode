from typing import List
from collections import Counter


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # Time: O(N)
        # Space: O(N)
        # N = len(nums)
        freq = [0] * (len(nums)+1)
        ans = []
        for num in nums:
            if freq[num] >= len(ans):
                ans.append([])
            ans[freq[num]].append(num)
            freq[num] += 1
        return ans

    def findMatrix2(self, nums: List[int]) -> List[List[int]]:
        # Time: O(N^2)
        # Space: O(N)
        # N = len(nums)
        numsCount = Counter(nums)
        freq = max(numsCount.values())
        ans = []
        for i in range(freq):
            cur = []
            for num, val in numsCount.items():
                if val >= freq - i:
                    cur.append(num)
            ans.append(cur)
        return ans
