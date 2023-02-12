# n = len(mat)
# m = len(mat[i])
# time: O(nlogm)
# space: O(n)
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """Function to return indices of the k weakest rows.

        Args:
            mat(List[List[int]]): a m*n binary matrix
            k(int): the number of indices to be returned

        Returns:
            List[int]: the infices of the k weakest rows in the matrix
        """
        count_1 = []
        for i in range(len(mat)):
            left = -1
            right = len(mat[i])
            while right - left > 1:
                mid = (left+right) // 2
                if mat[i][mid] == 1:
                    left = mid
                else:
                    right = mid
            count_1.append([right, i])
        count_1.sort()
        answer_list = []
        for i in range(k):
            answer_list.append(count_1[i][1])
        return answer_list
