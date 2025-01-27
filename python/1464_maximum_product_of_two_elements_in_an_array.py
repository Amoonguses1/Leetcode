from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """Function to return maximum value of (nums[i]-1)*(nums[j]-1)

        Args:
            nums(List[int]): natural numbers

        Returns:
            int: maximum value of product
        """
        # Time: O(N)
        # Space: O(1)
        # N = len(nums)
        """first, second = 0, 0
        for num in nums:
            if num > first:
                first, second = num, first
            elif num > second:
                second = num
        return (first-1) * (second-1)
        """
        # heap solution
        # Time: O(NlogN)
        # Space: O(N)
        # N = len(nums)
        def heapify(li, size_li, i):
            while i < size_li//2:
                if li[2*i+1] < li[2*i] and li[i] < li[2*i]:
                    li[i], li[2*i] = li[2*i], li[i]
                    i = 2*i
                elif li[2*i+1] >= li[2*i] and li[i] < li[2*i+1]:
                    li[i], li[2*i+1] = li[2*i+1], li[i]
                    i = 2*i+1
                else:
                    break

        def heapSort(li, size_li):
            for i in range(size_li//2, -1, -1):
                heapify(li, size_li, i)

        def extract(li, size_li):
            answer = li[0]
            li[0] = li[size_li-1]
            size_li -= 1
            heapSort(li, size_li)
            return answer

        heapSort(nums, len(nums))
        return (extract(nums, len(nums))-1)*(extract(nums, len(nums))-1)
