# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


def majorityElement(self, nums: List[int]) -> List[int]:
    """Function to find all the elements that appear more than ⌊ n/3 ⌋ times.
        Args:
            nums(List[int]): integer array
        Returns:
            List[int]: the elements that appear more than ⌊ n/3 ⌋ times.
    """
    if not nums:
        return []
    count1, count2, candidate1, candidate2 = 0, 0, 0, 1
    for n in nums:
        if n == candidate1:
            count1 += 1
        elif n == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = n, 1
        elif count2 == 0:
            candidate2, count2 = n, 1
        else:
            count1, count2 = count1 - 1, count2 - 1
    return [n for n in (candidate1, candidate2)
            if nums.count(n) > len(nums) // 3]
