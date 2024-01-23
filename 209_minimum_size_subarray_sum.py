

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(N)
        # Space: O(1)
        # N = len(nums)
        """
        if sum(nums) < target:
            return 0

        ans = len(nums)
        idx, res = 0, 0
        for i, num in enumerate(nums):
            res += nums[i]
            while target <= res:
                ans = min(ans, i-idx+1)
                res -= nums[idx]
                idx += 1
        return ans
        """
        # binary search
        # Time: O(NlogN)
        # Space: O(1)
        # N = len(nums)
        if sum(nums) < target:
            return 0

        left, right = -1, len(nums)
        while left < right - 1:
            mid = (left+right) // 2
            if self.windowFind(mid, nums, target):
                right = mid
            else:
                left = mid
        return right

    def windowFind(self, length, nums, target):
        if len(nums) < length or length < 1:
            return False

        res = sum(nums[:length-1])
        for i in range(length-1, len(nums)):
            res += nums[i]
            if res >= target:
                return True
            res -= nums[i-length+1]
        return False
