class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        track = [] # route
        used = [False] * len(nums)
        self.backtrack(nums, track, used)
        return self.res
        
    def backtrack(self, nums, track, used):
        if len(track) == len(nums):
            self.res.append(track.copy())
            return
        
        for i in range(len(nums)):
            if used[i] == True:
                continue
            
            track.append(nums[i]) #choose
            used[i] = True #mark
            self.backtrack(nums, track, used)
            track.pop() #cancel choose
            used[i] = False
