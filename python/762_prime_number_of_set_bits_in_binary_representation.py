# Time: O(N)
# Space: O(1)
# N = right - left


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        cnt = 0
        for i in range(left, right+1):
            strBin = str(bin(i))
            setBit = strBin.count("1")
            if setBit in primeList:
                cnt += 1
        return cnt
