class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort = sorted(nums) # O(NlogN)
        sub_len = 1
        res = 0

        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        for i in range(1, len(sort)):
            if sort[i] -1 == sort[i-1]:
                sub_len += 1

            elif sort[i] == sort[i-1]:
                continue
            else:
                sub_len = 1
            
            res = max(res, sub_len)
        res = max(res, sub_len)
        return res