class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs == [""]:
            return [[""]]
        freq = {}
        ans = []
        for i in range(len(strs)):
            s = [char for char in strs[i]]
            s.sort()
            s = "".join(s)
            if s in freq:
                freq[s].append(i)
            else:
                freq[s] = [i]

        for v in freq.values():
            group = []
            for i in v:
                group.append(strs[i])
            ans.append(group)
        return ans
            
        
    
if __name__ == "__main__":
    solution = Solution()
    strs = ["a"]
    result = solution.groupAnagrams(strs)
    print(result)