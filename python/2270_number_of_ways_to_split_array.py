# Time: O(N)
# Space: O(1)
# N = len(nums)


class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        total = sum(nums)
        pref = 0
        ans = 0
        for num in nums[:-1]:
            pref += num
            if total - pref <= pref:
                ans += 1
        return ans
