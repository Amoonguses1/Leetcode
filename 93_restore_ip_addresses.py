from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """Function to return all possible valid IP address

        Args:
            s(str): a string consist of digits only

        Returns:
            List[int]: all possible valid IP address
        """
        # simple brute force
        # Time: O(N^^3)
        # Space: O(N^^4)
        # N = len(s)
        """
        res = []
        length = len(s)
        for i in range(1, min(4, length)):
            if not self.is_valid(s[:i]):
                continue
            for j in range(i+1, min(i+4, length)):
                if not self.is_valid(s[i:j]):
                    continue
                for k in range(j+1, min(j+4, length)):
                    if not self.is_valid(s[j:k]) or not self.is_valid(s[k:]):
                        continue
                    res.append(s[:i]+"."+s[i:j]+"."+s[j:k]+"."+s[k:])
        return res

    def is_valid(self, s):
        if not s or (len(s) > 1 and s[0] == "0"):
            return False
        if int(s) > 255:
            return False
        return True
        """
        # Time: O(N^^4)
        # Space: O(N^^4)
        # N = len(s)
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if len(path) > 4:
            return

        if not s:
            if len(path) == 4:
                res.append(".".join(path))
        else:
            self.dfs(s[1:], path+[s[0]], res)
            if len(s) > 1 and s[0] != "0":
                self.dfs(s[2:], path+[s[:2]], res)
            if len(s) > 2 and s[0] != "0" and int(s[:3]) < 256:
                self.dfs(s[3:], path+[s[:3]], res)
