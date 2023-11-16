

class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer,
        rather than a nested list.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds,
        if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        pass

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds,
        if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        pass


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]

    def next(self) -> int:
        # Time: O(1)
        # Space: O(1)
        nested, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nested[i].getInteger()

    def hasNext(self) -> bool:
        # Time: O(M)
        # Space: O(1)
        # M is the depth of the nested list
        while self.stack:
            nested, i = self.stack[-1]
            if i == len(nested):
                self.stack.pop()
                continue
            if nested[i].isInteger():
                return True

            self.stack[-1][1] += 1
            self.stack.append([nested[i].getList(), 0])
        return False
