from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        n = len( nums ) - 1
        right = n
        flag = 0
        if nums[left] > nums[right] and nums[ left ] > target and nums[right] < target:
            return -1
        
        while flag < 1:
            if left == right or left == right - 1:
                flag += 1
            check = ( left + right ) // 2
            if nums[ check ] < nums[ right ]:
                right = check
            else:
                left = check
        # nums[right] is smallest
        if nums[ n ] == target:
            return n
        elif nums[ n ] < target:
            right -=1
            left = 0
        else:
            left = right
            right = n
        if nums[right] == target:
            return right
        while flag < 2:
            if left == right or left == right - 1:
                flag += 1
            check = ( left + right ) // 2
            if nums[ check ] ==target:
                return check
            elif nums[ check ] < target:
                left = check
            else:
                right = check
        return -1