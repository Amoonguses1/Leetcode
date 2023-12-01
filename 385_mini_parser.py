# Time: O(N)
# Space: O(N)
# N = len(s)

class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        if value:
            self.val = value
            self.li = None
        else:
            self.li = []
            self.val = None

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer,
        rather than a nested list.
        :rtype bool
        """
        return self.val is not None

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and
        adds a nested integer elem to it.
        :rtype void
        """
        self.val = None
        self.li = [elem]

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        self.val = value
        self.li = None

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds,
        if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return self.val

    def getList(self):
        """
        @return the nested list that this NestedInteger holds,
        if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return self.li


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        num, isNum, isMinus = 0, False, False
        stack = [NestedInteger()]
        for ch in s:
            if ch == "[":
                stack[-1].add(NestedInteger())
                stack.append(stack[-1].getList()[-1])
            elif ch == "," or ch == "]":
                if isNum:
                    if isMinus:
                        num *= -1
                        isMinus = False
                    isNum = False
                    stack[-1].add(NestedInteger(num))
                    num = 0
                if ch == "]":
                    stack.pop()
            elif ch == "-":
                isMinus = True
            else:
                isNum = True
                num = num*10 + int(ch)
        if isNum:
            if isMinus:
                num *= -1
            stack[-1].add(NestedInteger(num))
        return stack[0].getList()[0]
