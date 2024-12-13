# Time: O(m^2)
# Space: O(m)
from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        res = []
        numbers = [i for i in range(m, 0, -1)]
        for query in queries:
            res.append(m-1-numbers.index(query))
            numbers.remove(query)
            numbers.append(query)
        return res
