# Time: O(n)
# Space: O(n)


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """Function to find nth ugly number

        Args:
            n(int): a natural number

        Returns:
            int: the nth smallest ugly number
        """
        ugly = [1]
        pos2, pos3, pos5 = 0, 0, 0
        for _ in range(n-1):
            u2, u3, u5 = 2*ugly[pos2], 3*ugly[pos3], 5*ugly[pos5]
            Umin = min(u2, u3, u5)
            if Umin == u2:
                pos2 += 1
            if Umin == u3:
                pos3 += 1
            if Umin == u5:
                pos5 += 1
            ugly.append(Umin)
        return ugly[-1]
