# Time: O(N*M)
# Space: O(N)
# N = len(queries), M = the average length of queries
from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []
        for query in queries:
            i = j = 0
            while i < len(query):
                if j < len(pattern) and query[i] == pattern[j]:
                    i += 1
                    j += 1
                elif query[i].isupper():
                    break
                else:
                    i += 1
            if i == len(query) and j == len(pattern):
                ans.append(True)
            else:
                ans.append(False)
        return ans
