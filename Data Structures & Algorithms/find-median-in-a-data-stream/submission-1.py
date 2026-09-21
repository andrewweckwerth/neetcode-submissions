class MedianFinder:

    def __init__(self):
        self.li = list()
        
        

    def addNum(self, num: int) -> None:
        self.li.append(num)
        self.li.sort()

    def findMedian(self) -> float:
        length= len(self.li)
        if length%2==0:
            return (self.li[length//2] + self.li[-1 + length//2])/2
        else:
            return self.li[length//2]
        
        