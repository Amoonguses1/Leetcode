from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # blute-force
        # This solution is TLE in leetcode.
        # Time: O(N^2)
        # Space: O(N)
        # N = len(arr)
        ans = []
        diff = float("inf")
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                cur = abs(arr[j]-arr[i])
                if cur < diff:
                    ans = []
                    diff = cur
                if cur == diff:
                    ans.append(min(arr[i], arr[j]))
        ans.sort()
        return [[num, num+diff] for num in ans]

    def minimumAbsDifference2(self, arr: List[int]) -> List[List[int]]:
        # Time: O(NlogN)
        # Space: O(N)
        # N = len(arr)
        arr.sort()
        diff = float("inf")
        candi = []
        for i in range(len(arr)-1):
            cur = arr[i+1] - arr[i]
            if cur < diff:
                diff = cur
                candi = []
            if cur == diff:
                candi.append(arr[i])
        return [[num, num+diff] for num in candi]
