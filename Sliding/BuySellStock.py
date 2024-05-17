class Solution(object):
    def maxProfit(self, prices):
        r = 1
        l = 0
        prof = 0
        if len(prices) == 1:
            return 0
        while r < len(prices):
            if prices[l] < prices[r]:
                prof = max(prof, prices[r] - prices[l])
            else:
                l = r
            r += 1        
        return prof
    
if __name__ == "__main__":
    solution = Solution()
    prices = [2,4,1]
    result = solution.maxProfit(prices)
    print(result)