class Solution:
    def merge(self, intervals):

        #1. sort intervals by start time
        #2. compare current interval with last merged interval
        #3. Either a) merge b)start a new interval

        if not intervals:
            return []

        merged =[]
        intervals.sort(key= lambda x: x[0])

        prev = intervals[0]

        for interval in intervals[1:]:
            if  prev[1] >= interval[0]:
                prev[1] = max(prev[1], interval[1])
            else:
                merged.append(prev)
                prev = interval

        merged.append(prev)

        return merged