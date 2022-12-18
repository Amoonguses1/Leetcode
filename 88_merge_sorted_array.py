# time O(m+n)
# space O(1)
from typing import List


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int], n: int) -> None:
    """Function to merge two sorted array into one array
        Args:
            A(list[int]): list of integer
            B(list[int]): list of integer
            m(int): list size of A minus n
            n(int): list size of B
        Returns:
            None
    
    """
    a, b, write_index = m-1, n-1, m + n - 1

    while b >= 0:
        if a >= 0 and A[a] > B[b]:
            A[write_index] = A[a]
            a -= 1
        else:
            A[write_index] = B[b]
            b -= 1

        write_index -= 1