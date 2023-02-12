# Time: O(N)
# Space: O(N)
# N = len(self.countAndSay(n-1))


class Solution:
    def countAndSay(self, n: int) -> str:
        """Function to generate count-and-say string

        Args:
            n(int): how many times this function generate strings

        Returns:
            str: a generated string
        """
        if not isinstance(n, int):
            raise ValueError("Input must be an integer.")

        ans = "1"
        for _ in range(n-1):
            i = 0
            tmp = ""
            while i < len(ans):
                count = 1
                while i + 1 < len(ans) and ans[i+1] == ans[i]:
                    count += 1
                    i += 1
                tmp += str(count) + ans[i]
                i += 1
            ans = tmp
        return ans
