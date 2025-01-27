# Time: O(n)
# Space: O(1)


class Solution:
    def climbStairs(self, n: int) -> int:
        """Function to return how many distinct
            ways can you climb to the top
            Args:
                n(int): the number of steps in stairs
            returns:
                int: the number how many distinct ways
                    to climb to the top of the stairs
        """
        if n < 0:
            return

        cur = step_before = 1
        for _ in range(n):
            cur, step_before = step_before, cur + step_before
        return cur
