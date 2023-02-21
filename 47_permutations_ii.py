# Time: O(N!)
# Space: O(N!)
# N = len(nums)
from typing import List
import collections


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """Function to find all unique permutations

        Args:
            nums(List[int]): a list consist of integers

        Returns:
            List[List[int]]: all unique permutations
        """
        # sort solution
        """
        nums.sort()
        self.ans = []
        self.dfs(nums, [])
        return self.ans

    def dfs(self, nums, path):
        if not nums:
            self.ans.append(path)
        else:
            for i, num in enumerate(nums):
                if i > 0 and num == nums[i-1]:
                    continue
                self.dfs(nums[:i]+nums[i+1:], path+[num])
        """
        # dictionary solution
        num_dict = collections.Counter(nums)
        self.ans = []
        self.dfs(num_dict, nums, [])
        return self.ans

    def dfs(self, dic, nums, path):
        if len(path) == len(nums):
            self.ans.append(path)
        else:
            for key in dic:
                if dic[key] == 0:
                    continue
                dic[key] -= 1
                self.dfs(dic, nums, path+[key])
                dic[key] += 1
