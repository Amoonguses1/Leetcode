from typing import List


class Solution:
    def fairCandySwap(
            self, aliceSizes: List[int], bobSizes: List[int]
    ) -> List[int]:
        # two pointers
        # Time: O(NlogN + M logM)
        # Space: O(N+M)
        # N = len(aliceSizes), M = len(bobSizes)
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        alicePos, bobPos = 0, 0
        alices = sorted(list(set(aliceSizes)))
        bobs = sorted(list(set(bobSizes)))
        while alicePos < len(alices) and bobPos < len(bobs):
            cur = alices[alicePos] - bobs[bobPos]
            if cur == diff:
                return [alices[alicePos], bobs[bobPos]]

            if cur < diff:
                alicePos += 1
            else:
                bobPos += 1

    def fairCandySwap2(
            self, aliceSizes: List[int], bobSizes: List[int]
    ) -> List[int]:
        # blute force
        # Time: O(NM)
        # Space: O(1)
        # N = len(aliceSizes), M = len(bobSizes)
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        alices = set(aliceSizes)
        bobs = set(bobSizes)
        for alice in alices:
            if alice - diff in bobs:
                return [alice, alice-diff]

    def fairCandySwap3(
            self, aliceSizes: List[int], bobSizes: List[int]
    ) -> List[int]:
        # binary search
        # Time: O(NlogN + M logM)
        # Space: O(N+M)
        # N = len(aliceSizes), M = len(bobSizes)
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        aliceSizes.sort()
        bobSizes.sort()
        for num in aliceSizes:
            left, right = 0, len(bobSizes)
            target = num - diff
            while left < right:
                mid = (left+right)//2
                if bobSizes[mid] == target:
                    return [num, bobSizes[mid]]

                if bobSizes[mid] < target:
                    left = mid + 1
                else:
                    right = mid
        return [-1, -1]
