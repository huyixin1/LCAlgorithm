class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0

        while left < right:
            leng = right - left
            h = min(height[right], height[left])
            area = max(area, leng*h)
            if height[left] < height[right]: # move the shorter edge
                left += 1
            else:
                right -= 1

        return area