class TimeMap:

    def __init__(self):
        self.ma = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.ma:
            #self.ma[key][timestamp] = value
            self.ma[key].append((timestamp, value))
        else:
            self.ma[key] = [(timestamp, value)]
            #self.ma[key] = {timestamp: value}

        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.ma:
                return ""
        l, r = 0, len(self.ma[key])-1
        best = ""
        while(l<=r):
            search = (r + l)//2
            if self.ma[key][search][0] == timestamp:
                return self.ma[key][search][1]
            if self.ma[key][search][0] < timestamp:
                l = search+1
                best = self.ma[key][search][1]
            if self.ma[key][search][0] > timestamp:
                r = search -1 


        # if timestamp in self.ma[key]:
        #     return self.ma[key][timestamp]
        # while(!timestamp in self.ma[key]):
        #     timestamp-=1


        return best
        

        
