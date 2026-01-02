class Solution:
    def maxArea(self, height) -> int:
        result = 0
        
        left, right = 0, len(height) - 1
        while left < right:
            yo = min(height[left], height[right]) * (right - left)
            result = max(result,yo)

            if height[left] < height[right]: # move the smaller height
                left +=1
            else:
                right -= 1

        return result