

class Solution:
    def findNthDigit(self, n: int) -> int:
        # Time: O(log_10 n)
        # Space: O(1)
        digit = 1
        while n > digit * 9 * pow(10, digit-1):
            n -= digit * 9 * pow(10, digit-1)
            digit += 1
        num = pow(10, digit-1) + (n-1) // digit
        idx = (n-1) % digit
        return int(str(num)[idx])
