# Time: O(N)
# Space: O(1)
# N = len(height)
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Function to find the container which can store more water
            than any other containr
            Args:
                height(List[int]): the height of wall
            Returns:
                int: the maximum amount of water a container can store
        """
        if not height:
            raise ValueError("height must not be empty")

        for num in height:
            if not isinstance(num. int):
                raise ValueError("the list\"height\" must be int")

        start, end = 0, len(height) - 1
        vol = 0
        while end - start > 0:
            vol = max(vol, (end-start) * min(height[start], height[end]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return vol
