class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)
        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]: continue
                used[i] = True; path.append(nums[i]) # make choice
                dfs()
                used[i] = False; path.pop() # revoke

        dfs()
        return res