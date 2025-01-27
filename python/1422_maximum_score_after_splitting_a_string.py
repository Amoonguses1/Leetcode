# Time: O(N)
# Space: O(1)
# N = len(s)


class Solution:
    def maxScore(self, s: str) -> int:
        count_zeros = 0
        for ch in s:
            if ch == "0":
                count_zeros += 1

        count_left_zeros = 0
        count_right_ones = len(s) - count_zeros
        max_score = 0
        for i in range(len(s)-1):
            count_left_zeros += s[i] == "0"
            count_right_ones -= s[i] == "1"
            max_score = max(max_score, count_left_zeros+count_right_ones)
        return max_score
