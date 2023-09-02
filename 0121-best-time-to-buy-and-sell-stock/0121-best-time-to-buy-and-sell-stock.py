class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        best_buy = float('inf')
        for price in prices:
            best_buy = min(best_buy, price)
            max_profit = max(max_profit, price - best_buy)
        
        return max_profit
        
        
        # Slow 0(n^2)
        # for i in range(n):
        #     for j in range(i, n):
        #         max_profit = max(max_profit, prices[j] - prices[i])
        # return max_profit
        
        