class Solution(object):
    def myPow(self, x, n):
        """
        :type n: int
        :rtype: bool
        """
        r = 1
        b = x
        e = n
        
        while e > 0:
            if e % 2 == 1:
                r *= b
            b *= b
            e //= 2
        return r
    
if __name__ == "__main__":
    solution = Solution()
    x = 2.00000
    n = 10
    result = solution.myPow(x, n)
    print(result)