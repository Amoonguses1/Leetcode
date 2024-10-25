class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # Time: O(nlogn)
        # Space: O(logn)
        for i in range(2, n-1):
            st = self.Nthbase(n, i)
            if st != st[::-1]:
                return False
        return True

    def Nthbase(self, n, base):
        st = ""
        while n > 0:
            st += str(n % base)
            n //= base
        return st

    def isStrictlyPalindromic2(self, n: int) -> bool:
        return False
