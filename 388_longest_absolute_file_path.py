# Time: O(N)
# Space: O(N)
# N is the number of files or folders
from typing import List
from collections import defaultdict


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        """Function to find the longest absolute path
            Args:
                input(str):  may contain lowercase or uppercase English letters
                    , a new line character '\n', a tab character '\t'
                    a dot '.', a space ' ', and digits
            Returns:
                int:  the length of the longest absolute path to a file in the
                    abstracted file system
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
