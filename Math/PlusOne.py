class Solution(object):
    def plusOne(self, digits):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(len(digits)-1, -1, -1):
            print("index", i)
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits 
    
if __name__ == "__main__":
    solution = Solution()
    digits = [3,9,0,9]
    result = solution.plusOne(digits)
    print(result)