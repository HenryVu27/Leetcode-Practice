class Solution(object):
    def myPow(self, x, n):
        """
        :type n: int
        :rtype: bool
        """
        r = 1
        b = x
        e = n
        if n <= 0:
            e = 0-n
        while e > 0:
            if e % 2 == 1:
                r *= b
            b *= b
            e //= 2
        if n <= 0:
            r = 1/r
        return r
    
if __name__ == "__main__":
    solution = Solution()
    x = 2.00000
    n = -2
    result = solution.myPow(x, n)
    print(result)