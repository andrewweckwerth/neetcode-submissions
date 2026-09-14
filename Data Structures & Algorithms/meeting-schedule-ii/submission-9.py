"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # curr=0
        # ret=0
        # intervals.sort(key=lambda x: x.end)

        # ma = intervals[-1].end
        # print("adsf",ma)
        # intervals.sort(key=lambda x: x.start)
        if not intervals:
            return 0
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)

        # for i in intervals:
        #     start.append(i.start)
        #     end.append(i.end)
        # print("asdf",end)
        rooms = 0
        end_pointer =0
        for i in start:
            if i < end[end_pointer]:
                rooms += 1
            else:
                end_pointer += 1

        return rooms
        # ma = max(end)
        # loop = start + end
        # loop.sort()


        # for i in loop:
        #     if i in end:
        #         # curr-=end.count(i)
        #         curr-=1
        #     if i in start:
        #         curr+=1
        #         ret=max(curr, ret)
            
        return ret
        