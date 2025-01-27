from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # Time: O(N^3)
        # Space: O(N)
        # N = len(arr)
        prefix = [0]
        cur = 0
        for val in arr:
            cur ^= val
            prefix.append(cur)

        res = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j, len(arr)):
                    if prefix[i] ^ prefix[j] == prefix[j] ^ prefix[k+1]:
                        res += 1
        return res

    def countTriplets2(self, arr: List[int]) -> int:
        # Time: O(N^2)
        # Space: O(N)
        # N = len(arr)
        prefix = [0]
        cur = 0
        for val in arr:
            cur ^= val
            prefix.append(cur)

        res = 0
        for i in range(len(arr)):
            for k in range(i+1, len(arr)):
                if prefix[i] == prefix[k+1]:
                    res += k - i
        return res
