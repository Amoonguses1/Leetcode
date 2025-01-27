# time O(n)
# space O(1)
# n = len(nums)
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """Function to sort list in-place
          Args:
                nums(list[int]): list of integer
                the integers 0, 1, and 2 to represent
                the color red, white, and blue, respectively
            Returns:
                None
        """
        runner = 0
        left_part = 0
        right_part = len(nums) - 1
        while runner <= right_part:
            if nums[runner] == 0:
                nums[runner], nums[left_part] = nums[left_part], nums[runner]
                runner += 1
                left_part += 1
            elif nums[runner] == 1:
                runner += 1
            else:
                nums[runner], nums[right_part] = nums[right_part], nums[runner]
                right_part -= 1
        return
