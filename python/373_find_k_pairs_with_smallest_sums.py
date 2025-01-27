# Time: O(min(klogk, n1*n2log(n1*n2)) )
# Space: O(min(k, n1*n2))
# n1 = len(nums1), n2 = len(nums2)
from heapq import heappop
from heapq import heapify
from heapq import heappush
from typing import List


class Solution:
    def kSmallestPairs(self, nums1, nums2, k) -> List[List[int]]:
        """Function to find k smallest sum pairs

        Args:
            nums1(List[int]): a list of integers
            nums2(List[int]): a list of integers

        Returns:
            List[List[int]]: k smallest sum pairs
        """
        hq = []
        heapify(hq)
        for i in range(min(len(nums1), k)):
            heappush(hq, (nums1[i]+nums2[0], nums1[i], nums2[0], 0))
        out = []
        while k > 0 and hq:
            _, n1, n2, idx = heappop(hq)
            out.append((n1, n2))
            if idx + 1 < len(nums2):
                heappush(hq, (n1+nums2[idx+1], n1, nums2[idx+1], idx+1))
            k -= 1
        return out
