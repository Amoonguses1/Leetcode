# Time: O(2**N)
# Space: O(2**N)
# N = len(candidates)
from typing import List


class Solution(object):
    def combinationSum2(self, candidates, target) -> List[List[int]]:
        """Function to find all unique combinarions in candidates
            where the candidate numbers sum to target

        Args:
            candidates(List[int]): a list of integer
            1 <= candidates[i] <= 50
            target: a natural number
            1 <= target <= 30

        Returns:
            List[List[int]]: the list of all unique combinarions
        """
        ret = []
        self.dfs(sorted(candidates), target, 0, [], ret)
        return ret

    def dfs(self, nums, target, idx, path, ret):
        if target == 0:
            ret.append(path)
            return

        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            if nums[i] > target:
                break
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], ret)
