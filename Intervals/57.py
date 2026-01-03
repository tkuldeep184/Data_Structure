class Solution:
    def insert(self, intervals, newInterval):
        result = []

        for interval in intervals:
            #1. interval is before newInterval
            if interval[1]  < newInterval[0]:
                result.append(interval)

            #2. interval is after newInterval
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            
            #3. overlappigng
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        result.append(newInterval)
        return result
          