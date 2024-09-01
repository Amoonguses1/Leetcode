# Time: O(len(frac))
# Space: O(len(frac))
# frac is the length of answer


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        seen = dict()
        result = ""

        if numerator == 0:
            return "0"

        if (numerator < 0) ^ (denominator < 0):
            result += "-"
        numerator, denominator = abs(numerator), abs(denominator)

        ans = []
        cnt = 0
        loop = False

        while numerator != 0:
            if len(ans) == 1 or (len(ans) == 2 and ans[0] == "-"):
                ans.append(".")
                cnt += 1
            if seen.get(numerator, -1) >= 0:
                loop = True
                break
            if len(ans) != 0:
                seen[numerator] = cnt
            ans.append(str(numerator // denominator))
            numerator = numerator % denominator
            numerator *= 10
            cnt += 1

        if loop:
            pos = seen.get(numerator)
            result += "".join(ans[:pos]) + "("
            result += "".join(ans[pos:]) + ")"
        else:
            result += "".join(ans)
        return result
