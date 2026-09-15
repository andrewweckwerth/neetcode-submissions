class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        ret =  []
        interv= False
        i=0
        
        while i<len(intervals) and intervals[i][1] < newInterval[0]:
            ret.append(intervals[i])
            i+=1

        start = newInterval[0]
        end=newInterval[1]

        while i < len(intervals) and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        
        
        ret.append([start,end])

        while i<len(intervals):
            ret.append(intervals[i])
            i+=1


            # if not interv:
            #     start = min(newInterval[0], i[0])
            #     print("start", start)
            #     interv= True
            # if(i[1]<=newInterval[1]):
            #     continue
            # else:
            #     ret.append([start, max(newInterval[1], i[1])])
            # if i[0] > newInterval[1]:
            #     ret.append(i)
        return ret
        