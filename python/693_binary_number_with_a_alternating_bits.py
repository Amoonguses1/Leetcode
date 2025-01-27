# Time: O(logn)
# Space: O(logn)


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        old = ""
        for i in bin(n)[2:]:
            if old == i:
                return False

            old = i
        return True
