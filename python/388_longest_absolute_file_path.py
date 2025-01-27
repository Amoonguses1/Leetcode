# Time: O(N)
# Space: O(N)
# N is the number of files or folders
from typing import List
from collections import defaultdict


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        """Function to calculate the longest absolute path
            Args:
                input(str):  a string which means a directory structure
            Returns:
                int:  an integer which means the longest path length
        """
        maxlen = 0
        pathlen = defaultdict(int)
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth]+len(name))
            else:
                pathlen[depth+1] = pathlen[depth] + len(name) + 1
        return maxlen
