class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        leftMax = rightMax = 0

        while left < right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                area += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                area += rightMax - height[right]
                right -= 1
        return area