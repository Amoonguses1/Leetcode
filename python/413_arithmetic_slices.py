from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dif, old = float("inf"), float("inf")
        ans, cnt = 0, 0
        for num in nums:
            tmp_dif = num - old
            old = num
            if dif == tmp_dif:
                cnt += 1
            else:
                if cnt >= 3:
                    ans += ((cnt-2)*(cnt-1))//2
                cnt = 2
            dif = tmp_dif
        if cnt >= 3:
            ans += ((cnt-2)*(cnt-1))//2
        return ans
