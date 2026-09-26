"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        timesarr = []
        res = 0
        for i in intervals:
            timesarr.append([i.start,1])
            timesarr.append([i.end,0])

        timesarr.sort()
        count = 0

        for i in timesarr:
            if i[1] == 1:
                count += 1
            else:
                count -=1
            res = max(res, count)
        
        return res

