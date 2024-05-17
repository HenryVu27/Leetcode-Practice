class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
    
if __name__ == "__main__":
    solution = Solution()
    prices = [2,4,1]
    result = solution.maxProfit(prices)
    print(result)