# Time: O(N)
# Space: O(len(results))


class Solution:
    def decodeString(self, s: str) -> str:
        """Function to decode string
            Args:
                s(str): a encoded string
            Returns:
                str: a decoded string
        """
        if not s or len(s) == 0:
            return s
        result, _ = self.dfs(0, s, 0, '')
        return result

    def dfs(self, position, s, prev_num, prev_str):
        while position < len(s):
            while s[position].isdigit():
                prev_num = prev_num*10 + int(s[position])
                position += 1
            if s[position] == "[":
                returned_str, ending_pos = self.dfs(position+1,
                                                    s, prev_num=0, prev_str="")
                prev_str = prev_str + returned_str*prev_num
                position = ending_pos
                prev_num = 0
            elif s[position] == ']':
                return prev_str, position
            else:
                prev_str += s[position]
            position += 1
        return prev_str, position
