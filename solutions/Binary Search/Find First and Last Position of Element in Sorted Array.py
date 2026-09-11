class Solution:
    def searchRange(self, nums: List[int], target: int):
        return [self.leftBound(nums, target), self.rightBound(nums, target)]
    def leftBound(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid - 1
        if left >= len(nums) or nums[left] != target:
            return -1
        return left
    
    def rightBound(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if right < 0 or nums[right] != target: # why not equal
            return -1
        return right

