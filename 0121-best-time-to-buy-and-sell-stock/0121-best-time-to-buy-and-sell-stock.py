class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy, max_profit = float('inf'), 0
        
        for curr_price in prices:
            if curr_price < min_buy:
                min_buy = curr_price
            
            max_profit = max(max_profit, curr_price - min_buy)
        return max_profit