class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_Area = 0
        stack = []
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]]>h:
                height = heights[stack.pop()]
                width = i if not stack else i-stack[-1]-1
                max_Area = max(max_Area, height*width)
            stack.append(i)
        heights.pop()
        return max_Area