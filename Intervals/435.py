class Solution:
    def eraseOverlapIntervals(self, intervals):
        removed = 0

        intervals.sort(key = lambda x : x[1]) #sorting by end 
        
        prev = intervals[0]
        for interval in intervals[1:]:
            if max(prev[0], interval[0]) < min(prev[1],interval[1]):
                removed += 1
            
            else:
                prev = interval

        return removed