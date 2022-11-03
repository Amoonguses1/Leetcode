# time: O(NlogN)
# space: O(1)

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        n = len(nums_sorted)
        for i in range(n):
            left = i
            right = n
            mid = (left+right)//2
            found_flag = False
            while left < right - 1:
                if nums_sorted[i] + nums_sorted[mid] == target:
                    found_flag = True
                    break
                elif nums_sorted[i] + nums_sorted[mid] < target:
                    left = mid
                else:
                    right = mid
                mid = (left+right)//2
            indices_list = []
            if found_flag:
                for j in range(n):
                    if nums[j] == nums_sorted[i]:
                        indices_list.append(j)
                        break
                for j in range(n):
                    if nums[j] == nums_sorted[mid] and j != indices_list[0]:
                        indices_list.append(j)
                        break
                return indices_list
