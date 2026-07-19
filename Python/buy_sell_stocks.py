class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0 
        for i in prices :
            if i < buy :
                buy = i
            else :
                current_profit = i - buy
                profit = max(current_profit,profit)

        return profit
