from typing import List
from collections import deque


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        """Function to sort numbers in lexicographical order
            Args:
                n(int): The maximum number to sort from 1
            Returns:
                List[int]: All the numbers in the range [1, n]
                    sorted in lexicographical order.
        """
        # recursively use Trie
        # Time: O(n)
        # Space: O(1)
        # You don't count function call stack
        # in space complexity.
        """
        res = []
        if n < 10:
            return list(range(1, n+1))
        for i in range(1, 10):
            res.append(i)
            res += self.helper(i, n)
        return res

    def helper(self, start, n):
        res = []
        for aux in range(10):
            newStart = start*10+aux
            if newStart > n:
                break
            res .append(newStart)
            res += self.helper(newStart, n)
        return res
        """
        # DFS iterative
        # Time: O(n)
        # Space: O(log_10 n)
        ans = []
        for i in range(1, 10):
            cur = i
            if cur > n:
                break
            ans.append(cur)
            cur *= 10
            check_list = deque([cur+j for j in range(10)])
            while check_list:
                check = check_list.popleft()
                if check > n:
                    continue
                ans.append(check)
                for j in range(10):
                    check_list.appendleft(check*10+9-j)
        return ans
