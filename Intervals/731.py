class MyCalendarTwo:

    def __init__(self):
        self.overlap = []
        self.nonoverlap = []

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.overlap:
            if max(startTime, s) < min(endTime, e):
                '''ye wala tarika aur niche wlaa dono nuse kar sakte hai overlap k 
                liye but mujhe ye wala sahi laga aur visualze bhi ho ra hai'''
                return False

        for s, e in self.nonoverlap:
            if endTime > s and e > startTime:
                self.overlap.append(
                    (max(s,startTime), min(e, endTime))
                )
        
        self.nonoverlap.append((startTime,endTime))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)