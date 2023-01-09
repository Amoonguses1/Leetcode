# Time: O(N * 2^N)
# Space: O(N*2)
# N = len(expression)
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        """Function to calculate all possible results from computing
            all the different possible ways to group numbers and operators
            Args:
                expression(str): a string consist of numbers and operators
            Returns:
                List[int]: all possible results
        """
        for ch in expression:
            if ch.isdecimal():
                continue
            if ch in "+-*":
                continue
            raise ValueError("Invalid input")

        exp_dict = {}
        return self.recursion(expression, exp_dict)

    def recursion(self, exp, exp_dict):
        if exp in exp_dict:
            return exp_dict[exp]

        if exp.isdecimal():
            exp_dict[exp] = [int(exp)]
            return exp_dict[exp]

        ret = []
        for i, ch in enumerate(exp):
            if ch not in "+-*":
                continue
            left = self.diffWaysToCompute(exp[:i])
            right = self.diffWaysToCompute(exp[i+1:])
            ret.extend(eval(str(x)+ch+str(y)) for x in left for y in right)
        exp_dict[exp] = ret
        return ret
