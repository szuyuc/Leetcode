class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1 :
            return 0
        prv = float('inf')
        profit = 0
        for price in prices:
            if price > prv:
                profit += price-prv
            prv = price


        return profit
                