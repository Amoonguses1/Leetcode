from typing import List
import collections
# n = len(nums)-1


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Time: O(nlogn)
        # Space: O(n)
        # sort
        """
        li = sorted(nums)
        for i in range(len(li)-1):
            if li[i] == li[i+1]:
                return li[i]
        """
        # Time: O(n)
        # Space: O(n)
        # counter
        """
        dic = collections.Counter(nums)
        for key, val in dic.items():
            if val > 1:
                return key
        """
        # Time: O(n)
        # Space: O(1)
        # linked list
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
