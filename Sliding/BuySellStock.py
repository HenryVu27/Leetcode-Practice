class Solution(object):
    def maxProfit(self, prices):
        r = 1
        l = 0
        if len(prices) == 1:
            return 0
        for i in range(len(prices)-1):
            if prices[i] > prices[i+1]:
                l += 1
                r += 1
            else:
                r += 1
        prof = prices[r] - prices[l]
        return prof
    
if __name__ == "__main__":
    solution = Solution()
    
    result = solution.maxProfit(x, n)
    print(result)