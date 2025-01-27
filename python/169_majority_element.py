# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """Function to find majority element
            Args:
                nums(List[int]): the list of integer
            Returns:
                int: the number of majority element
        """
        if not nums:
            return

        major = nums[0]
        count = 1
        length = len(nums)
        for i in range(1, length):
            if count == 0:
                major = nums[i]
            if nums[i] == major:
                count += 1
            else:
                count -= 1
        return major
