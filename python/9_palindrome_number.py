# Time: O(N)
# Space: O(N)
# N = len(x)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        st = str(x)
        if st == st[::-1]:
            return True
        return False
