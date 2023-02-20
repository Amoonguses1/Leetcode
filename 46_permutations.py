# Time: O(N!)
# Space: O(N!)
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """Function to find  all the possible permutations

        Args:
            nums(List[int]): an integer list

        Returns:
            List[List[int]]: a list of all the possible permutations
        """
        self.ans = []
        self.dfs(nums, [])
        return self.ans

    def dfs(self, nums, path):
        if not nums:
            self.ans.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]])
        return
