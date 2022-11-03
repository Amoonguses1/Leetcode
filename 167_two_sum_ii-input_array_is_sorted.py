# time: O(nlogn) n is size of numbers
# space: O(1)
from typing import List


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums_length = len(numbers)
        indices_list = []
        for i in range(nums_length):
            left = i
            right = nums_length
            while left < right - 1:
                mid = (left + right) // 2
                if numbers[mid] == target - numbers[i]:
                    indices_list.append(i + 1)
                    indices_list.append(mid + 1)
                    return indices_list
                elif numbers[mid] < target - numbers[i]:
                    left = mid
                else:
                    right = mid
