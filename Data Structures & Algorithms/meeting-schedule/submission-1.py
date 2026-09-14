"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        ma=0
        for i in intervals:
            ma= max(ma, i.end)
        
        arr = [0]*ma
        for i in intervals:
            for j in range (i.start, i.end,1):
                if arr[j] == 1:
                    return False
                else:
                  arr[j] = 1
        
        return True
