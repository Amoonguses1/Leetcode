# Time: O(1)
# Space: O(1)


# The rand7() API is already defined for you.
def rand7():
    pass
# @return a random integer in the range 1 to 7


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        result = 40
        while result >= 40:
            result = 7 * (rand7()-1) + (rand7()-1)
        return result % 10 + 1
