# n = len(numbers)
# time: O(nlogn)
# space: O(1)
from typing import List


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Function to find indices of the two numbers
        which add up to target in binary search.

        Args:
            numbers(List[int]): list of integer
            target(int): integer
        
        Returns:
            List[int]: indices of the two numbers
        
        """
        if not numbers or target is None:
            raise ValueError("Your inputs don't fit.")

        nums_length = len(numbers)
        indices_list = []
        for i in range(nums_length):
            left = i
            right = nums_length
            while left < right - 1:
                mid = (left+right) // 2
                if numbers[mid] == target - numbers[i]:
                    indices_list.append(i+1)
                    indices_list.append(mid+1)
                    return indices_list

                elif numbers[mid] < target - numbers[i]:
                    left = mid
                else:
                    right = mid
            return []


# n = len(numbers)
# Time: O(n)
# Space: O(1)


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Function to find indices of the two numbers
        which add up to target in two pointers.

        Args:
            numbers(List[int]): list of integer
            target(int): integer

        Returns:
            List[int]: indices of the two numbers
        """
        if not numbers or target is None:
            raise ValueError("Your inputs don't fit.")

        left = 0
        right = len(numbers) - 1
        while left != right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]

            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return []
