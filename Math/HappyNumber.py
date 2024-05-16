class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n != 1:
            if n in s:
                return False
            s.add(n)
            n = sum([int(num)**2 for num in str(n)])
        return True            
        
    
if __name__ == "__main__":
    solution = Solution()
    n = 19
    result = solution.isHappy(n)
    print(result)