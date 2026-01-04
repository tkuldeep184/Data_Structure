class Solution:
    def findMinArrowShots(self, points) -> int:
        if not points:
            return 0

        arrows = 1
        points.sort()
        prev = points[0]

        for point in points[1:]:
            if max(prev[0], point[0]) <= min(prev[1], point[1]):
                # prev = (max(prev[0], point[0]),min(prev[1], point[1]))
                #yaha le list to tuple convert ho gaya is wajha se dikkat aa rahi hai 
                #correct way
                prev = [max(prev[0], point[0]), min(prev[1], point[1])]
                # prev[0] = max(prev[0], point[0])
                # prev[1] = min(prev[1], point[1])


            else:
                arrows += 1
                prev = point

        return arrows

