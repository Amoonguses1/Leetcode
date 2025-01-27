from typing import List


class Solution:
    def findMedianSortedArrays(
            self,
            nums1:
            List[int],
            nums2: List[int]
            ) -> float:
        # N = len(nums1), M = len(nums2)
        # Time: O(N+M)
        # Space: O(N+M)
        """
        len_1, len_2 = len(nums1), len(nums2)
        pos_1, pos_2 = 0, 0
        new = []
        while pos_1 < len_1 and pos_2 < len_2:
            if nums1[pos_1] < nums2[pos_2]:
                new.append(nums1[pos_1])
                pos_1 += 1
            else:
                new.append(nums2[pos_2])
                pos_2 += 1
        if pos_1 < len_1:
            new += nums1[pos_1:]
        else:
            new += nums2[pos_2:]
        ans, mid = 0, (len_1+len_2)//2 - 1
        if (len_1 + len_2) % 2 == 0:
            ans += new[mid]
        ans += new[mid+1]
        return ans if (len_1+len_2) % 2 else ans / 2
        """
        # N = len(nums1), M = len(nums2)
        # Time: O(log(M+N))
        # Space: O(1)
        length = len(nums1) + len(nums2)
        if length % 2 == 1:
            return self.kth(nums1, nums2, length//2)
        else:
            return (
                self.kth(nums1, nums2, length // 2)
                + self.kth(nums1, nums2, length // 2 - 1)
                ) / 2

    def kth(self, nums1, nums2, pos):
        if not nums1:
            return nums2[pos]
        if not nums2:
            return nums1[pos]
        mid_nums1, mid_nums2 = len(nums1) // 2, len(nums2) // 2
        medi_nums1, medi_nums2 = nums1[mid_nums1], nums2[mid_nums2]
        if mid_nums1 + mid_nums2 < pos:
            if medi_nums1 > medi_nums2:
                return self.kth(nums1, nums2[mid_nums2+1:], pos-mid_nums2-1)
            else:
                return self.kth(nums1[mid_nums1+1:], nums2, pos-mid_nums1-1)
        else:
            if medi_nums1 > medi_nums2:
                return self.kth(nums1[:mid_nums1], nums2, pos)
            else:
                return self.kth(nums1, nums2[:mid_nums2], pos)
