# Time: O(NlogN)
# Space: O(N)
from typing import List
import heapq


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """Function to invert score to rank

            Args:
                score(List[int]): a list of scores

            Returns:
                List[str]: a list of ranks
        """
        ranking = []
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i, val in enumerate(score):
            heapq.heappush(ranking, (-val, i))
        print(ranking)
        ans = [""] * len(score)
        for pos in range(len(score)):
            _, i = heapq.heappop(ranking)
            if pos < 3:
                ans[i] = rank[pos]
            else:
                ans[i] = str(pos+1)
        return ans
