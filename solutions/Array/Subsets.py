class Solution:
    def __init__(self):
        self.res = []
        self.track = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backwards(nums, 0)
        return self.res
        
    def backwards(self, nums, start) -> None:
        # preorder
        self.res.append(list(self.track))

        for i in range(start, len(nums)): # control not to look back
            self.track.append(nums[i]) # enter branch
            self.backwards(nums, i+1)
            self.track.pop() # leave branch, cancel choice