# Time: O(N)
# Space: O(1)
# N = len(nums)


class Solution:
    def canChoose(self, groups: list[list[int]], nums: list[int]) -> bool:
        length = len(nums)
        idx = pos = 0
        while pos < len(groups) and idx + len(groups[pos]) <= length:
            if self.isSameElementsSubArray(groups[pos], nums[idx:]):
                idx += len(groups[pos])
                pos += 1
            else:
                idx += 1

        return pos == len(groups)

    def isSameElementsSubArray(self, arr1: list[int], arr2: list[int]) -> bool:
        for i, num in enumerate(arr1):
            if num != arr2[i]:
                return False

        return True
