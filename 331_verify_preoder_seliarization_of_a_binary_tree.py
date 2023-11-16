# Time: O(N)
# Space: O(N)
# N = len(preorder)


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        li = preorder.split(",")
        stack = 1
        for st in li:
            stack -= 1
            if stack < 0:
                return False

            if st != "#":
                stack += 2
        return stack == 0
