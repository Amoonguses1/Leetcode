# Time: O(N)
# Space: O(1)
# N = len(s)


class Solution:
    def numDecodings(self, s: str) -> int:
        """Function to decode  an encoded message

        Args:
            s(str): a string consist of digits only

        Returns:
            int:  the number of ways to decode the given string
        """
        len_ = len(s)
        if len_ <= 0 or s[0] == "0":
            return 0

        nxt, cur, old = 0, 1, 1
        for i in range(1, len_):
            if 10 <= int(s[i-1:i+1]) <= 26:
                nxt += old
            if s[i] != "0":
                nxt += cur
            nxt, cur, old = 0, nxt, cur
        return cur
