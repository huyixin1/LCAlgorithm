class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1,len(nums)):
            res[i] = res[i-1]*nums[i-1]

        right = 1
        for i in range(len(nums)-2,-1,-1): # include first & last element 
            right *= nums[i+1]
            res[i] *= right
        if len(nums) < 3: # corner case
            res = reversed(nums)
        return res
