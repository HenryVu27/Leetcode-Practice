class Solution(object):
    def isHappy(self, digits):
        """
        :type n: int
        :rtype: bool
        """
        n = int("".join(map(str,digits))) + 1
        return [int(x) for x in str(n)]
    
if __name__ == "__main__":
    solution = Solution()
    digits = [3,9,0,9]
    result = solution.isHappy(digits)
    print(result)