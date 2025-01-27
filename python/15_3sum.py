# time O(n**2 logn)
# space O(n)
# n = len(nums)
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Function to find the triplets
        [nums[i], nums[j], nums[k]] such that
        i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0
        Args:
                nums(list[int]): list of integer
            Returns:
                List[List[int]] list of the triplets add up to 0
        """
        def recursionNsum(num_li, nth, target, result, results):
            if nth < 2 or len(num_li) < nth:
                return

            if nth == 2:
                left = 0
                right = len(num_li) - 1
                while left < right:
                    if num_li[left] + num_li[right] == target:
                        results.append(result+[num_li[left], num_li[right]])
                        left += 1
                        while left < right and num_li[left-1] == num_li[left]:
                            left += 1
                    elif num_li[left] + num_li[right] < target:
                        left += 1
                    else:
                        right -= 1
            else:
                for i in range(len(num_li)-nth+1):
                    if i == 0 or num_li[i-1] != nums[i]:
                        recursionNsum(num_li[i+1:], nth-1, target-num_li[i],
                                      result + [num_li[i]], results)
            return

        nums.sort()
        results = []
        recursionNsum(nums, 3, 0, [], results)
        return results
