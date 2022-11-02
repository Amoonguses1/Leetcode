#time: O(nlogn)
#space: O(1)
from typing import List


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers) - 1
        indices_list=[]
        for i in range(n):
            left = i + 1
            right = n
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == target - numbers[i]:
                    indices_list.append(i+1)
                    indices_list.append(mid+1)
                    return indices_list
                elif numbers[mid] < target - numbers[i]:
                    left = mid + 1
                else:
                    right = mid - 1
