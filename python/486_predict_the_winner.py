from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        """Function to predict the winner of the game
            Args:
                nums(List[int]): a list consist of natural numbers
            Returns:
                bool: whether player 1 win
        """
        # memorization
        # Time: O(N^2)
        # Space: O(N^2)
        # N = len(nums)
        if not nums:
            raise ValueError("Input something")

        for num in nums:
            if not num.isdecimal():
                raise ValueError("Invalid input")

        length = len(nums)
        memo = [[False] * length for i in range(length)]
        dp_sc = self.recursion(nums, 0, length-1, memo)
        if dp_sc < 0:
            return False

        return True

    def recursion(self, nums, start, end, m):
        if m[start][end]:
            return m[start][end]

        if start == end:
            m[start][end] = nums[end]
            return nums[end]

        m[start][end] = max(nums[start]-self.recursion(nums, start+1, end, m),
                            nums[end]-self.recursion(nums, start, end-1, m))
        return m[start][end]
