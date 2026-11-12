class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1,len(prices)):
            sell = prices[i]
            buy = min(prices[0:i])
            current_profit = sell - buy
            if(current_profit>max_profit):
                max_profit = current_profit
        return max_profit
            