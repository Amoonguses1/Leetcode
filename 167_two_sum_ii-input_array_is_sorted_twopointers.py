#Time: O(n)
#Space: O(1)
from typing import List

class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len( numbers ) - 1
        answer_list=[]
        while left != right:
            if numbers[left] + numbers[right] == target:
                answer_list.append(left+1)
                answer_list.append(right+1)
                return answer_list
            elif numbers[left] + numbers[right] < target:
                left+=1
            else:
                right-=1