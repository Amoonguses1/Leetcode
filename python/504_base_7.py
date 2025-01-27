# Time: O(log_7 num)
# Space: O(log_7 num)


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        neg = False
        if num < 0:
            neg = True
            num *= -1
        ans = ""
        while num > 0:
            ans = str(num % 7) + ans
            num //= 7
        if neg:
            return "-" + ans

        return ans
