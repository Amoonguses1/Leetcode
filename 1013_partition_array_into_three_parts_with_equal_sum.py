from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        # one-pass
        # Time: O(N)
        # Space: O(1)
        # N = len(arr)
        if sum(arr) % 3 != 0:
            return False

        target, cnt, cur = sum(arr)//3, 0, 0
        for num in arr:
            cur += num
            if cur == target:
                cur = 0
                cnt += 1
        return cnt > 2

    def canThreePartsEqualSum2(self, arr: List[int]) -> bool:
        # two pointers
        # Time: O(N)
        # Space: O(1)
        # N = len(arr)
        if sum(arr) % 3 != 0:
            return False

        left, right = 1, len(arr) - 2
        leftSum, rightSum = arr[0], arr[len(arr)-1]
        target = sum(arr) // 3
        while left < right:
            if leftSum != target:
                leftSum += arr[left]
                left += 1
            if left < right and rightSum != target:
                rightSum += arr[right]
                right -= 1
            if left <= right and rightSum == target and leftSum == target:
                return True
        return False
