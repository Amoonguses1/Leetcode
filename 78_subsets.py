# Time: O(pow(2,n))
# Space: O(pow(2,n))
# n = len(nums)
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Function to return all possible subsets from given array

        Args:
            nums(list[int]): an integer list

        Returns:
            List[List[int]]: all possible subsets
        """
        # bit manipulation
        """
        res = []
        for i in range(1<<len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & 1 << j:
                    tmp.append(nums[j])
            res.append(tmp)
        return res
        """
        # dfs
        self.ans, self.cur = [], []
        self.dfs(0, nums)
        return self.ans

    def dfs(self, start, nums):
        self.ans.append(self.cur.copy())
        for i in range(start, len(nums)):
            self.cur.append(nums[i])
            self.dfs(i+1, nums)
            self.cur.pop()
