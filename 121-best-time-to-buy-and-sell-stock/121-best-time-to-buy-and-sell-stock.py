class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                newProfit = prices[right] - prices[left]
                if newProfit > profit:
                    profit = newProfit
            else:
                left = right
            right += 1
        return profit
    