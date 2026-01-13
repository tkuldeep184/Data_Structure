class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        ans = 0
        for i in range(len(points) - 1):
            x = abs(points[i][0] - points[i+1][0])
            y = abs(points[i][1] - points[i+1][1])
            ans += max(x,y)
        return ans