# time: O(NlogN)
# space: O(1)

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        n = len(nums_sorted)
        for i in range(n):
            left = i+1
            right = n
            while left < right:
                mid = (left+right)//2
                if nums_sorted[i] + nums_sorted[mid] == target:
                    break
                elif nums_sorted[i] + nums_sorted[mid] < target:
                    left = mid+1
                else:
                    right = mid
            indices_list=[]
            if left != right:
                for j in range(n):
                    if nums[j] == nums_sorted[i]:
                        indices_list.append(j)
                        break
                for j in range(n):
                    if nums[j] == nums_sorted[(left+right)//2] and j != indices_list[0]:
                        indices_list.append(j)
                        break
                return indices_list
