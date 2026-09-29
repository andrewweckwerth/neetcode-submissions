class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        ret = [0 for _ in range(len(nums)-k+1)]



        heap = [(-nums[i], i) for i in range(k)]

        heapq.heapify(heap)
        
        ret[0]=-heap[0][0]
        

        # print(heap)
        for i in range(k, len(nums)):
            heapq.heappush(heap,(-nums[i],i))
            
            while(heap[0][1]<i-k+1):
                heapq.heappop(heap)
            # print(i,heap)
            ret[i-k+1]= -heap[0][0]

            

            

        return ret
        