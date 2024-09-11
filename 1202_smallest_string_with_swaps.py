from typing import List
from collections import defaultdict
# Time: O(NlogN)
# Space: O(N)
# N = len(s)


class Solution:
    def union(self, a, b):
        self.parent[self.find(a)] = self.find(b)

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.parent = list(range(len(s)))
        for a, b in pairs:
            self.union(a, b)

        group = defaultdict(lambda: ([], []))
        for i, ch in enumerate(s):
            parent = self.find(i)
            group[parent][0].append(i)
            group[parent][1].append(ch)

        res = [""] * len(s)
        for idx, chars in group.values():
            idx.sort()
            chars.sort()
            for ch, i in zip(chars, idx):
                res[i] = ch
        return "".join(res)
