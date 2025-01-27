# Time: O(N)
# Space: O(1)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Function to find the position of the first occurrence

            Args:
                haystack(str): the searched string
                needle(str): the target string
            Returns:
                int: the position of the string, called needle,
                    appeared the first occurrence
        """
        l_hay, l_needle = len(haystack), len(needle)
        for i in range(l_hay-l_needle+1):
            if haystack[i:i+l_needle] == needle:
                return i
        return -1
