class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for i in range(len(nums)):
            count[nums[i]] += 1

        for i in range(len(nums)):
            if i >=0 and i < count[0]:
                nums[i] = 0
            elif i >= count[0] and i < count[1]+count[0]:
                nums[i] = 1
            elif i >= count[1]+count[0]:
                nums[i] = 2
