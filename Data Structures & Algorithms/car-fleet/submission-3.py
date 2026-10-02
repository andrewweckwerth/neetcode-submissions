class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        both = []
        for i in range(len(position)):
            both.append((position[i], speed[i]))
        
        both.sort(reverse=True)
        # print(both)
        times = []

        
        for i in range(len(both)):

            # print("pos", both[i][0])
            # print("speed",both[i][1])
            time = (target-both[i][0])/both[i][1]

            # print("time", time)
            if not times or time > times[-1]:
                times.append(time)
            

        return len(times)



        