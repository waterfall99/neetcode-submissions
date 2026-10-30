class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        min_price = prices[0]
        highest_profit = 0
        while buy < (len(prices) - 1) and sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            elif prices[buy] <= prices[sell]:
                highest_profit = max(highest_profit, (prices[sell] - prices[buy]))
            sell += 1
        return highest_profit