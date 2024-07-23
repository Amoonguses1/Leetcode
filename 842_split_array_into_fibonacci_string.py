# Time: O(N^2)
# Space: O(N^2)
# N = len(num)
from typing import List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        # back tracking
        n = len(num)
        fin, res = [], []
        self.helper(0, res, n, fin, num)
        ans = []
        if len(fin) == 0:
            return []
        for i in fin[0]:
            ans.append(int(i))
        return ans

    def helper(self, pos, res, n, fin, num):
        if pos >= n and len(res) > 2:
            fin.append(res.copy())
            return

        cur = ""
        for i in range(pos, n):
            cur += num[i]
            if cur[0] == "0" and i != pos:
                break
            if int(cur) >= 2 ** 31:
                break

            if len(res) >= 2:
                if int(cur) == int(res[-1]) + int(res[-2]):
                    res.append(cur)
                    self.helper(i+1, res, n, fin, num)
                    res.pop()
            else:
                res.append(cur)
                self.helper(i+1, res, n, fin, num)
                res.pop()

    def splitIntoFibonacci2(self, num: str) -> List[int]:
        # iterative
        int_max = 2147483647
        ans = []
        for i in range(1, len(num)-2):
            first = num[:i]
            if len(first) != 1 and first[0] == "0":
                break
            if int(first) > int_max:
                break
            for j in range(i+1, len(num)-1):
                second = num[i:j]
                if len(second) != 1 and second[0] == "0":
                    break
                if int(second) > int_max:
                    break
                ans = [int(first), int(second)]
                idx = j
                while True:
                    cur = int(first) + int(second)
                    curLen = len(str(cur))
                    if cur > int_max or idx + curLen > len(num):
                        break
                    if cur != int(num[idx:idx+curLen]):
                        break
                    first, second = second, num[idx:idx+curLen]
                    ans.append(int(second))
                    idx += curLen
                    if idx == len(num):
                        return ans
                first = num[:i]
        return []
