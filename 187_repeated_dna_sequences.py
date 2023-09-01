# Time: O(N)
# Space: O(N)
from collections import defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """Find repeated 10-letter-sequences

        Given a string s that represents a DNA sequence,
        return all the 10-letter-long sequences (substrings)
        that occur more than once in a DNA molecule.

        Args:
            s(str): a DNA sequence that contains only 'A', 'T', 'G', and 'C'

        Returns:
            List[Str]: repeated 10-letter-sequences
        """
        counter = defaultdict(int)
        for i in range(len(s)-9):
            counter[s[i:i+10]] += 1
        return [s for s in counter.keys() if counter[s] > 1]
