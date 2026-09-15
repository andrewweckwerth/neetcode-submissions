class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        ret=0
        i=0
        while(i<len(intervals)-1):
            if(intervals[i][1]>intervals[i+1][0]):
                if(intervals[i][1]<intervals[i+1][1]):
                    intervals.pop(i+1)
                else:
                    intervals.pop(i)
                ret+=1
                continue
            i+=1
        return ret
        