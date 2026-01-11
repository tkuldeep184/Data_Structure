class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0]* (cols + 1) #stack flushing new concept
        max_area = 0

        for row in matrix:
            for i in range(cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0

        #largest rect in histogram leetcode
            stack = [-1]
            for i in range(cols + 1):
                while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)

        return max_area