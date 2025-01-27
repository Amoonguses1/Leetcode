# Time: O(N)
# Space: O(N)
from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # two pointers
        ans = [None] * len(nums)
        indices = [0, 1]
        for num in nums:
            ans[indices[num % 2]] = num
            indices[num % 2] += 2
        return ans

    def sortArrayByParityII2(self, nums: List[int]) -> List[int]:
        # in-place
        odds = []
        evens = []
        for i, num in enumerate(nums):
            if i % 2 == num % 2:
                continue
            if num % 2:
                if evens:
                    idx = evens.pop()
                    nums[i], nums[idx] = nums[idx], nums[i]
                else:
                    odds.append(i)
            else:
                if odds:
                    idx = odds.pop()
                    nums[i], nums[idx] = nums[idx], nums[i]
                else:
                    evens.append(i)
        return nums
