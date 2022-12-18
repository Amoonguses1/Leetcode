# time O(n**3 logn)
# space O(n)
# n = len(nums)
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """Function to find the quadruplets
        [nums[a], nums[b], nums[c], nums[d]] such that
          0 <= a, b, c, d < n
          a, b, c, and d are distinct.
          nums[a] + nums[b] + nums[c] + nums[d] == target
        Args:
                nums(list[int]): list of integer
                target(int): integer
            Returns:
                List[List[int]] list of the quadruplets add up to target
        """
        nums.sort()
        nums_length = len(nums)
        answer_list = []
        for i in range(nums_length):
            for j in range(i+1, nums_length):
                left = j + 1
                right = nums_length - 1
                adj_target = target - nums[i] - nums[j]
                if left >= right or adj_target < nums[left] * 2:
                    break
                if adj_target > nums[right] * 2:
                    continue
                temporary_list = [nums[i], nums[j], 0, 0]
                while left < right:
                    if nums[left] + nums[right] == adj_target:
                        temporary_list[2] = nums[left]
                        temporary_list[3] = nums[right]
                        left += 1
                        if temporary_list not in answer_list:
                            answer_list.append(temporary_list)
                            temporary_list = [nums[i], nums[j], 0, 0]
                    elif nums[left] + nums[right] < adj_target:
                        left += 1
                    else:
                        right -= 1
        return answer_list
