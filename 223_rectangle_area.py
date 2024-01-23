# Time: O(1)
# Space: O(1)


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int,
                    bx1: int, by1: int, bx2: int, by2: int) -> int:
        """Return total area covered by the two rectangles

        Given the coordinates of two rectilinear rectangles in a 2D plane,
        return the total area covered by the two rectangles.

        Args:
            ax1(int): x-coordinate of the lower left corner of the first
                rectangle
            ay1(int): y-coordinate of the lower left corner of the first
                rectangle
            ax2(int): x-coordinate of the upper right corner of the first
                rectangle
            ay2(int): y-coordinate of the upper right corner of the first
                rectangle
            bx1(int): x-coordinate of the lower left corner of the second
                rectangle
            by1(int): y-coordinate of the lower left corner of the second
                rectangle
            bx2(int): x-coordinate of the upper right corner of the second
                rectangle
            by2(int): y-coordinate of the upper right corner of the second
                rectangle

        Returns:
            int: total area covered by the two rectangles
        """
        dx = min(ax2, bx2) - max(ax1, bx1)
        dy = min(ay2, by2) - max(ay1, by1)
        area = 0
        if dx > 0 and dy > 0:
            area -= dx * dy
        area += (bx2-bx1) * (by2-by1)
        area += (ax2-ax1) * (ay2-ay1)
        return area
