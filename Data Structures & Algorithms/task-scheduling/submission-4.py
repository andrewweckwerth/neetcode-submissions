import heapq
import queue
class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = 0
        heap = [-freq for freq in Counter(tasks).values()]
        heapq.heapify(heap)


        time = 0
        cooldown = deque()
        
        while heap or cooldown:
            if not heap:
                time = max(time, cooldown[0][0])

            # Return tasks whose cooldown has finished.
            while cooldown and cooldown[0][0] <= time:
                _, remaining = cooldown.popleft()
                heapq.heappush(heap, remaining)

            remaining = heapq.heappop(heap) + 1

            if remaining < 0:
                cooldown.append((time + n + 1, remaining))

            time += 1

        return time





        #innefcient brute force method
        # ha = {}
        # cooldown = {}
        # for task in tasks:
        #     ha[task]= ha.get(task, 0)+1

        
        # count= 0
        # sorted(ha, reverse=True)
       
        # ne = next(iter(ha.keys()), None)

        # while len(ha)>0:
        #     count+=1
        #     # print(ha)
        #     # print(ne)
        #     if ne == None:
        #         pass
        #     elif ha[ne]==1:
        #         del ha[ne]
                
        #     else:
        #         ha[ne]-=1
                
        #         cooldown[ne] = n+1
        #     sorted(ha, reverse=True)
            


        #     for item in list(cooldown):
        #         if cooldown[item]<=1:
        #             del cooldown[item]
        #         else:
        #             cooldown[item]-=1

        #     # while ne not in cooldown:
        #     #     ne = next(iter(ha.keys()), None)
        #     ne = next((task for task in ha if task not in cooldown), None)


        # return count