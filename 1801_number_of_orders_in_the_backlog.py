# Time: O(NlogN)
# Space: O(N)
# N = len(orders)
from typing import List
from heapq import heappop, heappush


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy, sell = [], []
        for price, amount, order in orders:
            if order:
                heappush(sell, (price, amount))
            else:
                heappush(buy, (-1*price, amount))

            while buy and sell and -buy[0][0] >= sell[0][0]:
                buyOrder, sellOrder = heappop(buy), heappop(sell)
                if buyOrder[1] > sellOrder[1]:
                    heappush(buy, (buyOrder[0], buyOrder[1] - sellOrder[1]))
                if sellOrder[1] > buyOrder[1]:
                    heappush(sell, (sellOrder[0], sellOrder[1] - buyOrder[1]))
        return sum(amount for _, amount in buy+sell) % 1000000007
