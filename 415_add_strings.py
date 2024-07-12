# Time: O(n+m)
# Space: O(max(n+m))
# n = len(num1), m = len(num2)


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]
        ans = ""
        carry = i = 0
        maxLength = max(len(num1), len(num2))
        while i < maxLength or carry:
            num1digit = int(num1[i]) if i < len(num1) else 0
            num2digit = int(num2[i]) if i < len(num2) else 0
            cur = (num1digit + num2digit + carry)
            carry = cur // 10
            ans += str(cur % 10)
            i += 1
        return ans[::-1]
