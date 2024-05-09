class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        freq = {}
        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in freq:
                return [freq[num2], i]
            freq[nums[i]] = i
        return []
    
if __name__ == "__main__":
    solution = Solution()
    nums = [2,7,11,15]
    target = 9
    result = solution.twoSum(nums, target)
    print(result)