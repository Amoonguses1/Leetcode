from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # blute force
        # Time: O(nlogn)
        # Space: O(n)
        return [bin(i).count("1") for i in range(n+1)]

    def countBits2(self, n: int) -> List[int]:
        # Time: O(n)
        # Space: O(n)
        count = [0]
        for i in range(1, n+1):
            count.append(count[i >> 1] + i % 2)
        return count
