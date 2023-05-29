from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """Function to compare two version numbers

        Args:
            version1(str): a string consist of digits and dots
            version2(str): a string consist of digits and dots

        Returns:
            int: if version1 > version2, return 1
            if version1 < version2, return -1
            otherwise, return 0
        """
        # Time: O(max(m,n))
        # Space: O(max(m,n))
        # m, n = len(version1), len(version2)
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))
        for v1_num, v2_num in zip_longest(v1, v2, fillvalue=0):
            if v1_num == v2_num:
                continue
            return -1 if v1_num < v2_num else 1

        return 0

    def compareVersion2(self, version1: str, version2: str) -> int:
        # Time: O(max(m,n))
        # Space: O(1)
        # m, n = len(version1), len(version2)
        i, j, v1_len, v2_len = 0, 0, len(version1), len(version2)
        while i < v1_len or j < v2_len:
            num1, nIndx1 = self.getNum(version1, i, v1_len)
            num2, nIndx2 = self.getNum(version2, j, v2_len)
            if num1 < num2:
                return -1

            if num1 > num2:
                return 1

            i, j = nIndx1, nIndx2
        return 0

    def getNum(self, st, start, end):
        num, i = 0, start
        for i in range(start, end):
            if st[i] == ".":
                break
            num *= 10
            num += int(st[i])
        return num, i+1
