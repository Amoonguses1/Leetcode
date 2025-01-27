from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Function to find indices of the two numbers
        such that they add up to target.
        Args:
            nums(list[int]): list of integer
            target(int): integer
        Returns:
            list[int]: indices of the two numbers
        Raises:
            ValueError
        """
        """
        # binary search
        # n = len(nums)
        # time: O(nlogn)
        # space: O(1)
        if nums is None or target is None:
            return None

        from_num_to_idx = {}
        for idx, num in enumerate(nums):
            if target - num in from_num_to_idx:
                return [from_num_to_idx[target - num], idx]

            from_num_to_idx[num] = idx
        nums_sorted = sorted(nums)
        nums_length = len(nums_sorted)
        for i in range(nums_length):
            left = i
            right = nums_length
            mid = (left+right)//2
            found_flag = False
            while left < right - 1:
                if nums_sorted[i] + nums_sorted[mid] == target:
                    found_flag = True
                    break
                elif nums_sorted[i] + nums_sorted[mid] < target:
                    left = mid
                else:
                    right = mid
                mid = (left+right)//2
            indices_list = []
            if found_flag:
                for j in range(nums_length):
                    if nums[j] == nums_sorted[i]:
                        indices_list.append(j)
                        break
                for j in range(nums_length):
                    if nums[j] == nums_sorted[mid] and j != indices_list[0]:
                        indices_list.append(j)
                        break
                return indices_list

        raise ValueError(f"No combination of nums '{nums}' can be the target '{target}'.")
        """
        # hash map
        # n = len(nums)
        # time: O(n)
        # space: O(n)
        if nums is None or target is None:
            return None

        from_num_to_idx = {}
        for idx, num in enumerate(nums):
            if target - num in from_num_to_idx:
                return [from_num_to_idx[target - num], idx]

            from_num_to_idx[num] = idx

        raise ValueError(f"No combination of nums '{nums}' can be the target '{target}'.")