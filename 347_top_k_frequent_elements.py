import heapq
from collections import Counter
from typing import List


class FrequentElements:
    def find_k_frequent_elements(self, nums: List[int], k: int) -> List[int]:
        """Function to find the k most frequent elements.

        Args:
            nums(list[int]): list of integer
            target(int): integer

        Returns:
            list[int]: the k most frequent elements in any order

        Raises:
            TypeError
        """
        # heap
        # time: O(nlogk)
        # space: O(n)
        # n := len(nums)
        if type(nums) is not list:
            raise TypeError("The type of the input nums should be list")

        if type(k) is not int:
            raise TypeError("The type of the input k should be integer")

        if not nums or not k:
            return []

        if len(set(nums)) <= k:
            return list(set(nums))
        """
        from_num_to_count = Counter(nums)
        count_heap = []
        for num, count in from_num_to_count.items():
            heapq.heappush(count_heap, (count, num))
            if len(count_heap) > k:
                heapq.heappop(count_heap)

        k_frequent_elements = []
        while count_heap:
            count, num = heapq.heappop(count_heap)
            k_frequent_elements.append(num)

        return k_frequent_elements
        """
        # merge
        # time: O(nlogn)
        # space: O(n)
        # n := len(nums)
        def mergeSort(li):
            if len(li) < 2:
                return li

            mid = len(li) // 2
            left = mergeSort(li[:mid])
            right = mergeSort(li[mid:])
            return merge(left, right)

        def merge(li1, li2):
            cnt_1, cnt_2 = 0, 0
            merged = []
            while cnt_1 < len(li1) and cnt_2 < len(li2):
                if li1[cnt_1][1] > li2[cnt_2][1]:
                    merged.append(li1[cnt_1])
                    cnt_1 += 1
                else:
                    merged.append(li2[cnt_2])
                    cnt_2 += 1
            if cnt_1 < len(li1):
                merged.extend(li1[cnt_1:])
            if cnt_2 < len(li2):
                merged.extend(li2[cnt_2:])
            return merged

        dict_nums = Counter(nums)
        arr = []
        for ele in dict_nums.keys():
            arr.append([ele, dict_nums[ele]])
        sorted_arr = mergeSort(arr)
        answer = []
        for i in range(k):
            answer.append(sorted_arr[i][0])
        return answer
