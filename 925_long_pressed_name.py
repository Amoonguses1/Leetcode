# Time: O(N)
# Space: O(1)
# N = len(typed)


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        namePos = 0
        for ch in typed:
            if namePos < len(name) and ch == name[namePos]:
                namePos += 1

            if namePos == 0 or ch != name[namePos-1]:
                return False

        return namePos == len(name)
