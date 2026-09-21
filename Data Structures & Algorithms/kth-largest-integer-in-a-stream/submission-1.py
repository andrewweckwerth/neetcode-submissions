import heapq
class KthLargest:

    # def __init__(self, k: int, nums: List[int]):
    #     self.nums = sorted(nums)
    #     self.k=k        

    # def add(self, val: int) -> int:
    #     self.nums.append(val)
    #     self.nums = sorted(self.nums)
    #     return self.nums[-self.k]
        
    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.min_heap = nums
        heapq.heapify(self.min_heap)

        while(len(self.min_heap)>k):
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        while(len(self.min_heap)>self.k):
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
