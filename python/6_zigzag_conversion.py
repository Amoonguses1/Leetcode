# Time: O(N)
# Space: O(N)
# N = len(s)


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """Function to 'zigzag convert' a given string

            Args:
                s(str): a string
                numRows(int): nonnegative integer

            Returns:
                str: a converted string
        """
        if numRows == 1:
            return s

        jump, res = numRows - 1, ""
        for i in range(numRows):
            for j in range(0, len(s)-i, 2*jump):
                res += s[i+j]
                if i and i != jump and j - i + 2*jump < len(s):
                    res += s[j-i+2*jump]
        return res
