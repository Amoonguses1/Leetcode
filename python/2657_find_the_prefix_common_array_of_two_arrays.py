# Time: O(N)
# Space: O(N)
# N = len(A)
from typing import List


class Solution:
    def findThePrefixCommonArray(
            self, A: List[int], B: List[int]
    ) -> List[int]:
        not_pair = set()
        cnt = 0
        ans = []
        for i in range(len(A)):
            if A[i] not in not_pair:
                not_pair.add(A[i])
            else:
                cnt += 1
            if B[i] not in not_pair:
                not_pair.add(B[i])
            else:
                cnt += 1
            ans.append(cnt)
        return ans
