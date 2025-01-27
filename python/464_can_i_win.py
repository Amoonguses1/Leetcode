# Time: O(N!)
# Space: O(N!)
# N = maxRange


class Solution:
    def canIWin(self, maxRange: int, target: int) -> bool:
        if target <= 0:
            return True

        if maxRange*(maxRange+1) // 2 < target:
            return False

        self.memo = {}

        return self.canWin(tuple(range(1, maxRange+1)), target)

    def canWin(self, choices, target):
        if choices[-1] >= target:
            return True

        if choices in self.memo:
            return self.memo[choices]

        for i, num in enumerate(choices):
            if not self.canWin(choices[:i]+choices[i+1:], target-num):
                self.memo[choices] = True
                return True

        self.memo[choices] = False
        return False
