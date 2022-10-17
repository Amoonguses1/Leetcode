from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_sorted = sorted(nums)
        left = 0
        right = len( new_sorted ) - 1
        while True:
            if new_sorted[ left ] + new_sorted[ right ] == target:
                break
            elif new_sorted[ left ] + new_sorted[ right ] < target:
                left += 1
            else:
                right -= 1
        answer_list=[]
        for i in range( len(nums ) ):
            if nums[i] == new_sorted[left]:
                answer_list.append(i)
                break
        for i in range( len(nums ) ):
            if nums[i] == new_sorted[right] and i != answer_list[0]:
                answer_list.append(i)
                break
        return answer_list