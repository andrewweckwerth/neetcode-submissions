class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        

        while(len(heap)>1):
            s1 = -1 * heapq.heappop(heap)
            s2 = -1 * heapq.heappop(heap)
            
            re = s1-s2
            print(s1, s2, re)
            if re:
                heapq.heappush(heap, -1*re)
            
        if heap:
            return -1*heap[0]
        return 0


