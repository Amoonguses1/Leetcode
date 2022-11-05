# time: O(nlogn) n is size of numbers
# space: O(1)
from typing import List


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums_length = len(numbers)
        indices_list = []
        for i in range(nums_length):
            left = i
            right = nums_length
            while left < right - 1:
                mid = (left+right) // 2
                if numbers[mid] == target - numbers[i]:
                    indices_list.append(i+1)
                    indices_list.append(mid+1)
                    return indices_list

                elif numbers[mid] < target - numbers[i]:
                    left = mid
                else:
                    right = mid


# Time: O(n) n is size of numbers
# Space: O(1)


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        answer_list = []
        while left != right:
            if numbers[left] + numbers[right] == target:
                answer_list.append(left+1)
                answer_list.append(right+1)
                return answer_list

            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
