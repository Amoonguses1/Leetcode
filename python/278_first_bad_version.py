# time: O(logn)
# space: O(1)


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """Function to find the first version which causes error.

        Args:
            n(int): integer
        Return:
            int: an index of the first version which causes error
        """
        if n is None:
            raise ValueError("error!")

        left = 0
        right = n + 1
        while left < right - 1:
            now = (left+right) // 2
            if isBadVersion(now):
                right = now
            else:
                left = now
        return right
