class Solution:
    def minimumOperations(self, num: str) -> int:
        # blute force
        # Time: O(N^2)
        # Space: O(1)
        # N = len(num)
        ans = len(num)
        for i in range(len(num)-1, -1, -1):
            for j in range(i-1, -1, -1):
                cur = int(num[i]) + int(num[j]) * 10
                if cur % 25 == 0:
                    ans = min(ans, len(num)-j-2)
                    break
            if num[i] == "0":
                ans = min(ans, len(num)-1)
        return ans

    def minimumOperations2(self, num: str) -> int:
        # Time: O(N)
        # Space: O(1)
        # N = len(num)
        foundFive, foundZero = False, False
        idx = len(num)
        for i, ch in enumerate(num[::-1]):
            if foundFive and ch in ["2", "7"]:
                idx = i
                break
            if foundZero and ch in ["0", "5"]:
                idx = i
                break
            if ch == "5":
                foundFive = True
            if ch == "0":
                foundZero = True
        return idx - 1 if idx != len(num) or foundZero else idx
