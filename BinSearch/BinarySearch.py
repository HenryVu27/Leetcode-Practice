class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxR = 0
        for i, num in enumerate(nums):
            if i > maxR:
                return False
            maxR = max(maxR, i + num)
        return True
        
if __name__ == "__main__":
    solution = Solution()
    nums = []
    result = solution.canJump(nums)
    print(result)