

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Time: O(sqrt(n))
        # Space: O(1)
        # blute force solution
        if n < 3:
            return 1

        cnt = 0
        for i in range(1, n):
            cnt += i
            if cnt == n:
                return i

            if cnt > n:
                return i - 1

    def arrangeCoins2(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        # binary search solution
        left, right = 0, n+1
        while left < right:
            mid = (left+right) // 2
            cur = mid*(mid+1)//2
            if cur == n:
                return mid

            if cur < n:
                left = mid + 1
            else:
                right = mid
        return left - 1
