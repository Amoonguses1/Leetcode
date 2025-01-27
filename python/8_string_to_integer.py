# Time: O(N)
# Space: O(N)
# N = len(s)


class Solution:
    def myAtoi(self, s: str) -> int:
        """Function to a string to an integer

            Args:
                s(str): string

            Returns:
                int: an integer converted from string
        """
        if not isinstance(s, str):
            raise ValueError("Input must be a string")

        ans, isNegative = 0, 1
        isStarted = False
        for ch in s.strip():
            if ch.isdigit():
                ans = ans*10 + int(ch)
            else:
                if ch not in ["+", "-"] or isStarted:
                    break
                if ch == "-":
                    isNegative = -1
            isStarted = True
        ans = max(min(ans*isNegative, pow(2, 31) - 1), -pow(2, 31))
        return ans
