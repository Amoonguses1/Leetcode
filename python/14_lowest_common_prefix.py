from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Time: O(MN)
        # Space: O(M)
        # N = len(strs), M=len(strs[0])
        """
        ans = ""
        for i in range(len(strs[0])):
            ch = strs[0][i]
            br = False
            for st in strs:
                if i >= len(st) or st[i] != ch:
                    br = True
                    break
            if br:
                break
            else:
                ans += ch
        return ans
        """
        # Time: O(NlogN)
        # Space: O(M)
        # N = len(strs), M = max(len(str) for str in strs)
        words = sorted(strs)
        first, last = words[0], words[-1]
        ans = ""
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans
