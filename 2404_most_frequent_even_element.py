from collections import Counter
from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        """Function to the most frequent even element.
            Args:
                nums(List[int]): an integer list
            Returns:
                int: the most frequent even element
        """
        # Time: O(NlogN)
        # Space: O(1)
        # N = len(nums)
        """
        nums.sort()
        answer = -1
        counted = 0
        current_count = 0
        current_target = -1
        for i in nums:
            if i % 2:
                continue
            if i == current_target:
                current_count += 1
            else:
                current_count = 1
                current_target = i
            if current_count > counted:
                    counted = current_count
                    answer = current_target
        return answer
        """
        # Time: O(N)
        # Space: O(N)
        # N =len(nums)
        nums_dict = Counter(nums)
        ans = -1
        num = 0
        for key, value in nums_dict.items():
            if key % 2:
                continue
            if value > num:
                ans = key
                num = value
            elif value == num:
                if key < ans:
                    ans = key
        return ans
