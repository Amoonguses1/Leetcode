class Solution:
    def twoEggDrop(self, n: int) -> int:
        # recursive solution
        # Time: O(n^2)
        # Space: O(n)
        self.ans = dict()
        return self.helper(n, 2)

    def helper(self, n, eggs):
        if eggs == 1:
            return n

        if n == 0:
            return 0

        if (n, eggs) in self.ans:
            return self.ans[(n, eggs)]

        cur = float("inf")
        for i in range(1, n+1):
            cur = min(cur, 1 + max(self.helper(i-1, eggs-1),
                      self.helper(n-i, eggs)))
        self.ans[(n, eggs)] = cur
        return cur

    def twoEggDrop2(self, n: int) -> int:
        # mathmatical solution
        # Time: O(sqrt(n))
        # Space: O(1)
        cur = 0
        for i in range(1, n):
            cur += i
            if cur >= n:
                return i
        return n
