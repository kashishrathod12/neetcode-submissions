class Solution:
    def maxArea(self, heights: List[int]) -> int:
        Max_Area = min(heights[0], heights[-1]) * (len(heights)-1)
        left = 0
        right = len(heights)-1
        while left<right:
            area = min(heights[left], heights[right]) * (right - left)
            if Max_Area<area:
                Max_Area = area
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return Max_Area
        