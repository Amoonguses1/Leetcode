# Time: O(N)
# Space: O(N)
# N is the digits of num1 and num2 in binary notation


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num1BitCount = bin(num1).count('1')
        num2BitCount = bin(num2).count('1')
        res = num1
        for i in range(32):
            if num1BitCount > num2BitCount and (1 << i) & num1:
                res ^= 1 << i
                num1BitCount -= 1
            if num1BitCount < num2BitCount and (1 << i) & num1 == 0:
                res ^= 1 << i
                num1BitCount += 1
        return res

    def minimizeXor2(self, num1: int, num2: int) -> int:
        setBitNum2 = str(bin(num2)).count("1")
        strNum1 = str(bin(num1))[2:]
        ans = []
        for ch in strNum1:
            if setBitNum2 > 0 and ch == "1":
                ans.append("1")
                setBitNum2 -= 1
            else:
                ans.append("0")

        pos = 0
        ans = ans[::-1]
        length = len(ans)
        for _ in range(setBitNum2):
            while pos < length and ans[pos] == "1":
                pos += 1
            if pos < length:
                ans[pos] = "1"
            else:
                ans.append("1")

        return int("".join(ans[::-1]), 2)
