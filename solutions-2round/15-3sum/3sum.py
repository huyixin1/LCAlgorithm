class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)-2):
            # precut, remove duplicate set
            if i > 0 and nums[i] == nums[i-1]: continue
            s = - nums[i] # fix one num
            l, r = i+1, len(nums)-1
            while l < r:
                
                if nums[l] + nums[r] == s:
                    res.append([nums[i], nums[l], nums[r]])
                    # need to move too, may find several sets
                    l += 1
                    r -= 1
                    # pre cut skip the same item
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l] + nums[r] > s:
                    r -= 1
                else:
                    l += 1
        
        return res

            