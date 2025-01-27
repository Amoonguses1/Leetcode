from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        """Function to find indices such that nums[i] == target
            Args:
                grid(list[list[int]]): list of integer
                sorted in non-increasing order both row-wise and column-wise
            Returns:
                int: the number of negative numbers in list
        """
        """
        # sorting solution
        # time O(nlogn)
        # space O(1)
        # n = len(nums)

        if nums is None:
            return

        nums.sort()
        answer_list = []
        for i in range( len( nums ) ):
            if nums[i] == target:
                answer_list.append(i)
        return answer_list

        """
        # time O(n)
        # space O(1)
        # n = len(nums)
        if nums is None:
            return

        less = count = 0
        for i in nums:
            if i == target:
                count += 1
            elif i < target:
                less += 1
        ans = []
        for i in range(count):
            ans.append(less)
            less += 1
        return ans
