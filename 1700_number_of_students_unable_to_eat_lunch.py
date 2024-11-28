from typing import List
from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Time: O(N)
        # Space: O(1)
        # N = len(students)
        orders = [0, 0]
        for preference in students:
            orders[preference] += 1

        for sandwich in sandwiches:
            if orders[sandwich] == 0:
                break

            orders[sandwich] -= 1

        return sum(orders)

    def countStudents2(
            self, students: List[int], sandwiches: List[int]
    ) -> int:
        # Time: O(N^2)
        # Space: O(N)
        # N = len(students)
        stu_queue = deque(students)
        sand_queue = deque(sandwiches)

        while True:
            length = len(stu_queue)
            for _ in range(length):
                order = stu_queue.popleft()
                if order != sand_queue[0]:
                    stu_queue.append(order)
                else:
                    sand_queue.popleft()

            if length == len(stu_queue):
                return len(stu_queue)
