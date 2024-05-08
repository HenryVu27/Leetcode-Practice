class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq = {}
        for i in nums:
            if i in freq:
                return True
            else:
                freq[i] = 0
        
        return False


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 1]
    result = solution.containsDuplicate(nums)
    print(result)