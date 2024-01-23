# Time: O(N)
# Space: O(1)
# N = len(data)
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        count = 0
        for datum in data:
            if count == 0:
                if (datum >> 5) == 0b110:
                    count = 1
                elif (datum >> 4) == 0b1110:
                    count = 2
                elif (datum >> 3) == 0b11110:
                    count = 3
                elif (datum >> 7) != 0:
                    return False

            else:
                if (datum >> 6) != 0b10:
                    return False

                count -= 1
        return count == 0
