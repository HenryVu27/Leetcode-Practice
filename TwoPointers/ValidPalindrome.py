class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """        
        s = ''.join(ch for ch in s if ch.isalnum()).lower()
        if s == "":
            return True
        b = 0
        e = len(s)-1
        print(s)
        while b <= e:
            if s[b] != s[e]:
                return False
            b += 1
            e -= 1
        return True
    
if __name__ == "__main__":
    solution = Solution()
    s = "abba"
    result = solution.isPalindrome(s)
    print(result)