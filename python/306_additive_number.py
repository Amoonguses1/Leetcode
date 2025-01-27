# Time: O(N^3)
# Space: O(N)
# N = len(num)


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n):
            if num[0] == "0" and i > 1:
                break
            for j in range(i+1, n):
                first = int(num[:i])
                if num[i] == "0" and j > i+1:
                    break
                second = int(num[i:j])
                pos = j
                while pos < n:
                    tmp = first + second
                    if num[pos:].startswith(str(tmp)):
                        pos += len(str(tmp))
                        first = second
                        second = tmp
                    else:
                        break
                if pos == n:
                    return True
        return False
