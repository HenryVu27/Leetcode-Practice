class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = [char for char in s]
        t = [char for char in t]
        s.sort()
        t.sort()
        if s == t:
            return True
        return False
            
        
    
if __name__ == "__main__":
    solution = Solution()
    s = "rat"
    t = "ra"
    result = solution.isAnagram(s, t)
    print(result)