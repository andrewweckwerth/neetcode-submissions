import heapq
class MedianFinder:

    # def __init__(self):
    #     self.li = list()
        
        

    # def addNum(self, num: int) -> None:
    #     self.li.append(num)
    #     self.li.sort()

    # def findMedian(self) -> float:
    #     length= len(self.li)
    #     if length%2==0:
    #         return (self.li[length//2] + self.li[-1 + length//2])/2
    #     else:
    #         return self.li[length//2]


    def __init__(self):
        # self.li = list()
        self.min_heap = []
        self.max_heap = []
        
        
        
        

    def addNum(self, num: int) -> None:
        
        

        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else: 
            heapq.heappush(self.max_heap, -num)

       
        
        if len(self.max_heap)-len(self.min_heap) > 1:
            heapq.heappush(self.min_heap, -1 * heapq.heappop(self.max_heap))
        if len(self.min_heap)-len(self.max_heap) > 1:
            heapq.heappush(self.max_heap,-1* heapq.heappop(self.min_heap))

        # print(self.max_heap)
        # print(self.min_heap)
        # print("\n")

    def findMedian(self) -> float:
        count = len(self.min_heap) + len(self.max_heap)
        if count == 0 :
            return 0
        if count % 2 == 0:
            return (-1*self.max_heap[0] + self.min_heap[0])/2

        else: 
            
            if len(self.max_heap)>len(self.min_heap):
                return -1*self.max_heap[0]
            elif len(self.min_heap)==0:
                return 0
            else:
                return self.min_heap[0]
                
        
        
        