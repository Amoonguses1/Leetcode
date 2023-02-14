# Time: O(N**target)
# Space: O(N**target)
# N = len(candidates)
from typing import List


class Solution:
    def combinationSum(self, candidates, target) -> List[List[int]]:
        """Function to find all combinations which add up to target

        Args:
            candidates(List[int]): distinct natural numbers
            (1 <= candidates.length <= 30, 2 <= candidates[i] <= 40)
            target: a natural number

        Returns:
            List[List[int]]
        """
        ans = []
        self.dfs(candidates, target, [], ans)
        return ans

    def dfs(self, nums, target, path, ans):
        if target <= 0:
            if target == 0:
                ans.append(path)
            return

        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ans)
