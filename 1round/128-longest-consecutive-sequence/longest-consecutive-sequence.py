class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set(nums)
        for x in s:
            
            if x-1 in s:
                continue
        
            # x is the beginning of this sequence
            length = 0
            while x in s:
                length += 1
                x += 1
            res = max(res, length)

        return res