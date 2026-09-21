import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        min_heap = []

        for pair in points:
            dist = math.sqrt((pair[0])**2 + (pair[1])**2)
            print(dist)
            heapq.heappush(min_heap,(-dist,pair))
        
            if(len(min_heap)>k):
                heapq.heappop(min_heap)
        
        return [pair for dist, pair in min_heap]
