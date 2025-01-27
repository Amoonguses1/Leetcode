# Time: O(1)
# Space: O(1)


class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if children > money:
            return -1

        money -= children
        cnt = money // 7
        mod = money % 7
        if cnt == children - 1 and mod == 3 and cnt > 0:
            cnt -= 1
        if cnt > children or (cnt == children and mod > 0):
            cnt = children - 1
        return cnt
