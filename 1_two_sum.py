from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        left = 0
        right = len(nums_sorted) - 1
        while True:
            if nums_sorted[left] + nums_sorted[right] == target:
                break
            elif nums_sorted[left] + nums_sorted[right] < target:
                left += 1
            else:
                right -= 1
        indices_list=[]
        for i in range(len(nums )):
            if nums[i] == nums_sorted[left]:
                indices_list.append(i)
                break
        for i in range(len(nums )):
            if nums[i] == nums_sorted[right] and i != indices_list[0]:
                indices_list.append(i)
                break
        return indices_list
