class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        fs = {}
        for i in s:
            if i not in fs:
                fs[i] = 1
            else:
                fs[i] += 1
        for i in t:
            if i not in fs:
                return False
            if i in fs:
                fs[i] -= 1
                if fs[i] == 0:
                    del fs[i]
        if len(fs) == 0:
            return True
        return False
            
        
    
if __name__ == "__main__":
    solution = Solution()
    s = "rat"
    t = "ra"
    result = solution.isAnagram(s, t)
    print(result)