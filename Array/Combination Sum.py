class Solution:
    def __init__(self):
            self.res = []
            self.track = []
            self.trackSum = 0

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return self.res
        self.backtrack(candidates, 0, target)
        return self.res

    def backtrack(self, nums, start, target) -> None:
        if self.trackSum == target:
            self.res.append(list(self.track)) # add to result (why have to turn to list)
            return 
        if self.trackSum > target: # not applicable
            return
        for i in range(start, len(nums)):
            self.trackSum += nums[i]
            self.track.append(nums[i])

            self.backtrack(nums, i, target) # iterate from index:i

            self.trackSum -= nums[i]
            self.track.pop()

        
