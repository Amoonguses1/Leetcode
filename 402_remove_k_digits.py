

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Time: O(n)
        # Space: O(n)
        st = []
        for n in num:
            while st and k and st[-1] > n:
                st.pop()
                k -= 1
            if st or n is not "0":
                st.append(n)
        if k:
            st = st[:-k]
        return ''.join(st) or '0'
