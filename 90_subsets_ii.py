# Time: O(2 ^^ n)
# Space: O(2 ^^ n)
# n = len(nums)
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """Function to return all subsets without any duplicates

        Args:
            nums(List[int]): an integer array

        Returns:
            List[List[int]]: the list of subsets without any duplicates
        """
        nums.sort()
        ans = []
        self.dfs(nums, ans, [])
        return ans

    def dfs(self, nums, res, path):
        res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[i+1:], res, path+[nums[i]])
