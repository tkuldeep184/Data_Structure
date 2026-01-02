class Solution:
    def getLeftArray(self, height, n):
        LeftMax = [0] * n

        LeftMax[0] = height[0]

        for i in range(1,n):
            LeftMax[i] = max(LeftMax[i-1], height[i])

        return LeftMax

    def getRightArray(self, height, n):
        RightMax = [0] * n

        RightMax[n-1] = height[n-1]

        for i in range(n - 2 ,-1 ,-1):
            RightMax[i] = max(RightMax[i+1], height[i])

        return RightMax


    def trap(self, height) -> int:
        n = len(height)
        if n == 0:
            return 0

        LeftMax = self.getLeftArray(height, n)
        RightMax = self.getRightArray(height, n)       

        total = 0 

        for i in range(n):
            width = 1
            h = min(LeftMax[i], RightMax[i]) - height[i]
            total = total + h
        
        return total

