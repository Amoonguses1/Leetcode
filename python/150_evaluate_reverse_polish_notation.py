# Time: O(N)
# Space: O(N)
# N =len(tokens)
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """Function to calculate formula formatted by reverse Polish notation

            Args:
                tokens(List[str]): list consist of numbers and operands

            Returns:
                int: the answer of formula
        """
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                continue
            for st in token:
                if st in "-":
                    continue
                if st not in [str(i) for i in range(10)]:
                    raise ValueError("token must be operands and numbers")

        stack = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                tmp = stack.pop()
                if token == "+":
                    stack[-1] += tmp
                elif token == "-":
                    stack[-1] -= tmp
                elif token == "*":
                    stack[-1] *= tmp
                else:
                    check = stack[-1] % tmp
                    stack[-1] //= tmp
                    if stack[-1] < 0 and check:
                        stack[-1] += 1
            else:
                stack.append(int(token))
        return stack[0]
