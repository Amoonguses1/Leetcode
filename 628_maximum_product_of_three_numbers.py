from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Time: O(nlogn)
        # Space: O(n)
        # n = len(nums)
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

    def maximumProduct2(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        # n = len(nums)
        maxArr = [float("-inf")] * 3
        minArr = [0, 0]
        for num in nums:
            for i, maxNum in enumerate(maxArr):
                if num > maxNum:
                    maxArr = maxArr[:i] + [num] + maxArr[i:-1]
                    break
            for i, minNum in enumerate(minArr):
                if num < minNum:
                    minArr = minArr[:i] + [num] + minArr[i:-1]
                    break
        product = maxArr[0] * maxArr[1] * maxArr[2]
        product = max(product, minArr[0] * minArr[1] * maxArr[0])
        return product
