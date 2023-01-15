class Solution:
    MOD = 1000000007

    def countGoodNumbers(self, n: int) -> int:
        """Function to calculate the number of strings
            consist of "good numbers"
            Args:
                n(int): an interger which stands for
                    the length of strings
            Returns:
                int: the number of strings modulo 10^9+7
        """
        if not isinstance(n, int):
            raise ValueError("n must be an integer")

        # Time:O(logN)
        # Space:O(1)
        """
        res = pow(20, n//2, 10**9+7)
        if n % 2:
            res = (res*5) % (10**9+7)
        return res
        """
        # recursive solution
        # Time:O(logN)
        # Space:O(logN)
        ret = self.power(20, n//2) % self.MOD
        if n % 2:
            return (5*ret) % self.MOD

        else:
            return ret

    def power(self, m, n):
        if n == 0:
            return 1

        ret = self.power(m, n//2) % self.MOD
        if n % 2:
            ret = (((ret**2) % self.MOD) * m) % self.MOD
        else:
            ret = (ret**2) % self.MOD
        return ret
