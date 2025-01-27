from typing import List
import copy


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # mathmatical solution
        # Time: O(rowIndex)
        # Space: O(rowIndex)
        ans = [1]
        prev = 1
        for i in range(1, rowIndex+1):
            val = prev * (rowIndex - i + 1) // i
            ans.append(val)
            prev = val
        return ans

    def getRow2(self, rowIndex: int) -> List[int]:
        # DP
        # Time: O(rowIndex^2)
        # Space: O(rowIndex^2)
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        ans, nextRow = [1, 1], [1]
        for i in range(rowIndex-1):
            for i in range(1, len(ans)):
                nextRow.append(ans[i-1]+ans[i])
            nextRow.append(1)
            ans, nextRow = copy.deepcopy(nextRow), [1]
        return ans
