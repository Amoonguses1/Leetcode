# Time: O(NlogN)
# Space: O(N)
# N = len(nums)
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """Function to calculate the largest number.
            Args:
                nums(List[int]): a list of non-negative intergers
            Returns:
                str: the string of the largest number
        """
        if not nums:
            return

        def merge_sort(nums):
            if len(nums) <= 1:
                return nums

            length = len(nums) // 2
            left = merge_sort(nums[:length])
            right = merge_sort(nums[length:])
            return merge(left, right)

        def merge(left, right):
            result = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if (int(str(left[i]) + str(right[j])) >
                   int(str(right[j]) + str(left[i]))):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            while i < len(left):
                result.append(left[i])
                i += 1
            while j < len(right):
                result.append(right[j])
                j += 1
            return result

        new_nums = merge_sort(nums)
        return str(int("".join(map(str, new_nums))))
