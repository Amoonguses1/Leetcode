# Time: O(N)
# Space: O(N)
# N = len(deck)
from typing import List
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        res = [0] * n
        indices = deque(range(n))

        for card in deck:
            idx = indices.popleft()
            res[idx] = card
            if indices:
                indices.append(indices.popleft())

        return res
