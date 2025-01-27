# Time: O(NlogM)
# Space: O(1)
# N = len(candies), M = total_candies // k


class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        total_candies = sum(candies)
        if total_candies < k:
            return 0

        max_candies = total_candies // k + 1
        min_candies = 0
        while max_candies > min_candies:
            mid = (max_candies+min_candies) // 2
            if self.canDistributeCandies(candies, mid, k):
                min_candies = mid + 1
            else:
                max_candies = mid
        return min_candies - 1

    def canDistributeCandies(self, candies, div, people) -> bool:
        cnt = 0
        for candy in candies:
            cnt += candy // div
        return cnt >= people
