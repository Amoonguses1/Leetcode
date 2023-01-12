# Time: O(logn)
# Space: O(logn)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """Function to calculate pow(x,n)
            Args:
                x(float): a real number
                n(int): an integer
            Returns:
                float: the answer of pow(x,n)
        """
        if not isinstance(x, float):
            raise ValueError("x needs to be inputted type float.")

        if not isinstance(n, int):
            raise ValueError("n needs to be inputted type int.")

        res = self.dp(x, abs(n))
        return float(res) if n > 0 else 1/res

    def dp(self, base, exp):
        if exp == 0:
            return 1

        if exp % 2 == 0:
            return self.dp(base*base, exp//2)

        else:
            return self.dp(base*base, exp//2) * base
