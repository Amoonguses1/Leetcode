# Time: O(N)
# Space: O(N)
# N = len(nums)


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []

        start = cur = nums[0]
        ans = []
        for i in range(1, len(nums)):
            if nums[i] == start:
                continue

            if not self.isNext(cur, nums[i]):
                self.addNewRange(ans, start, cur)
                start = nums[i]
            cur = nums[i]

        # Handle the last range
        self.addNewRange(ans, start, cur)
        return ans

    def isNext(self, cur: int, nextNum: int) -> bool:
        return cur + 1 == nextNum

    def addNewRange(self, ans: list[str], start: int, end: int):
        if start == end:
            ans.append(str(start))
        else:
            ans.append(str(start)+"->"+str(end))
        return
