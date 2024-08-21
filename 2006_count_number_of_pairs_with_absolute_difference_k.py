from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # hash solution
        # Time: O(N)
        # Space: O(N)
        # N = len(nums)
        seen = dict()
        cnt = 0
        for num in nums:
            cnt += seen.get(num-k, 0)
            cnt += seen.get(num+k, 0)
            if num not in seen:
                seen[num] = 0
            seen[num] += 1
        return cnt

    def countKDifference2(self, nums: List[int], k: int) -> int:
        # blute force
        # Time: O(N^2)
        # Space: O(1)
        cnt = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    cnt += 1
        return cnt
