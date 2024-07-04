

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Time: O(sqrt(num))
        # Space: O(1)
        for i in range(num+1):
            if i ** 2 == num:
                return True
            if i ** 2 > num:
                return False

    def isPerfectSquare2(self, num: int) -> bool:
        # Time: O(log num)
        # Space: O(1)
        # bianry search solution
        if num == 1:
            return True

        left, right = 0, num
        while left < right:
            mid = (left+right)//2
            if mid**2 == num:
                return True

            if mid ** 2 > num:
                right = mid
            else:
                left = mid + 1
        return False
