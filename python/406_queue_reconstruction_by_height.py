# Time: O(NlogN)
# Space: O(N)
# N = len(people)
from typing import List
from operator import itemgetter


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """Function to reconstruct the queue
            Args:
                people(list[List[int]]): each list represents the person's
                    height and how many people in front who have a height
                    greater than or equal to his/her.
            Returns:
                List[List[int]]: the queue
        """
        sorted_order = sorted(people, key=itemgetter(1))
        sorted_height = sorted(sorted_order, key=itemgetter(0), reverse=True)
        answer_list = []
        for li in sorted_height:
            answer_list.insert(li[1], li)
        return answer_list
