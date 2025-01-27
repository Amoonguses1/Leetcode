from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """
        # Time: O(2 ^^ N)
        # Space: O(N)
        # N = len(nums)
        max_bit = 1 << len(nums)
        ans = []
        for i in range(max_bit):
            curArr = []
            for j in range(len(nums)):
                if i & 1 << j:
                    if len(curArr) > 0 and nums[j] < curArr[-1]:
                        continue
                    curArr.append(nums[j])
            if len(curArr) < 2 or curArr in ans:
                continue
            ans.append(curArr)
        return ans
        """

        # Time: O(N^2)
        # Space: O(N)
        # N = len(nums)
        curr = [[nums[0]]]
        for x in nums[1:]:
            curr += [y+[x] for y in curr if x >= y[-1]]
            curr += [[x]]
        curr = [tuple(x) for x in curr if len(x) >= 2]
        return list(set(curr))
