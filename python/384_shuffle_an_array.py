from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.li = nums

    def reset(self) -> List[int]:
        # Time: O(1)
        # Space: O(1)
        return self.li

    def shuffle(self) -> List[int]:
        # Time: O(N)
        # Space: O(N)
        # N = len(self.li)
        ans = self.li[:]
        for i in range(len(ans)):
            swap_num = random.randrange(i, len(ans))
            ans[i], ans[swap_num] = ans[swap_num], ans[i]
        return ans
