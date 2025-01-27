# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [0] * n
        for i in range(1, n+1):
            if i % 15 == 0:
                ans[i-1] = "FizzBuzz"
            elif i % 3 == 0:
                ans[i-1] = "Fizz"
            elif i % 5 == 0:
                ans[i-1] = "Buzz"
            else:
                ans[i-1] = str(i)
        return ans

    def fizzBuzz2(self, n: int) -> List[str]:
        # solution without % operator
        ans = [str(i+1) for i in range(n)]
        i, fizz, buzz = 0, 0, 0
        while i < n:
            fizz += 1
            buzz += 1
            if fizz == 3 and buzz == 5:
                ans[i] = "FizzBuzz"
                fizz = buzz = 0
            elif fizz == 3:
                ans[i] = "Fizz"
                fizz = 0
            elif buzz == 5:
                ans[i] = "Buzz"
                buzz = 0
            i += 1
        return ans
