from typing import List
from collections import deque
from collections import defaultdict


class Solution:
    def minMutation(
            self, startGene: str, endGene: str, bank: List[str]
            ) -> int:
        # DFS solution
        # Time: O(N^2)
        # Space: O(N)
        # N = len(bank)
        """
        stack = [[startGene, 1]]
        gene = ["A", "G", "C", "T"]
        geneDist = defaultdict(lambda: 100)
        geneDist[startGene] = 0
        while stack:
            tmp, cnt = stack.pop()
            for i in range(8):
                for ch in gene:
                    candi = tmp[:i] + ch + tmp[i+1:]
                    if candi in bank and cnt < geneDist[candi]:
                        stack.append([candi, cnt+1])
                        geneDist[candi] = cnt
        if geneDist[endGene] == 100:
            geneDist[endGene] = -1
        return geneDist[endGene]
        """
        # BFS solution
        # Time: O(N)
        # Space: O(N)
        # N = len(bank)
        bankSet = set(bank)
        options = ['A', 'C', 'G', 'T']
        queue = deque([startGene])
        visited = set([startGene])
        count = 0
        while queue:
            size = len(queue)
            for i in range(size):
                gene = queue.popleft()
                if gene == endGene:
                    return count

                for j in range(8):
                    for option in options:
                        newGene = gene[:j] + option + gene[j+1:]
                        if newGene in bankSet and newGene not in visited:
                            visited.add(newGene)
                            queue.append(newGene)
            count += 1
        return -1
