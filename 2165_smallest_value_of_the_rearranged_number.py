# Time: O(NlogN)
# Space: O(N)
# N = log(num)


class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        negative = 1
        if num < 0:
            negative = -1
            num *= -1
        stack = []
        while num != 0:
            stack.append(num % 10)
            num //= 10
        stack.sort()

        if negative < 0:
            return self.constructNegativeNum(stack)
        else:
            return self.constructPositiveNum(stack)

    def constructNegativeNum(self, stack: list[int]) -> int:
        ans = 0
        for i in range(len(stack)-1, -1, -1):
            ans *= 10
            ans += stack[i]
        ans *= -1
        return ans

    def constructPositiveNum(self, stack: list[int]) -> int:
        idx = self.findNotZero(stack)
        ans = stack[idx] * pow(10, idx)
        for i in range(idx+1, len(stack)):
            ans *= 10
            ans += stack[i]
        return ans

    def findNotZero(self, nums: list[int]) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left+right) // 2
            if nums[mid] != 0:
                right = mid
            else:
                left = mid + 1
        return left
