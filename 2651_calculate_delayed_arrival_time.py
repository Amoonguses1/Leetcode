# Time: O(1)
# Space: O(1)


class Solution:
    def findDelayedArrivalTime(
            self, arrivalTime: int, delayedTime: int
    ) -> int:
        return (arrivalTime + delayedTime) % 24
