class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        check = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in check:
                if stack and stack[-1] == check[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if stack: return False
        return True if not stack else False
            
        
    
if __name__ == "__main__":
    solution = Solution()
    s = "()"
    result = solution.isValid(s)
    print(result)