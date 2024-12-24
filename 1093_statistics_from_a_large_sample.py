# Time: O(N)
# Space: O(1)
# N = len(count)
from typing import List


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        maxFreq = 0
        min_val, max_val = len(count), 0
        total = total_elements = mode = 0
        for i, val in enumerate(count):
            total_elements += val
            if maxFreq < val:
                mode = i
                maxFreq = val

            if val != 0:
                min_val = min(i, min_val)
                max_val = i
                total += i * val

        median_ind = (total_elements+1) // 2
        cur = prev = median = 0
        found = False
        odd = total_elements % 2
        notFoundMedian = True
        for i, val in enumerate(count):
            cur += val
            if cur >= median_ind and notFoundMedian:
                if cur >= median_ind + 1 or odd:
                    notFoundMedian = False
                    median = i

                if found:
                    notFoundMedian = False
                    median = (prev+i) / 2

                found = True
                prev = i
                median_ind += 1
        return [min_val, max_val, total/total_elements, median, mode]
