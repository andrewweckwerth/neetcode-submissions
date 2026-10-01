class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ret = [0 for _ in range(len(temperatures))]

        stack = deque()


        for i, t in enumerate(temperatures):

            while stack and stack[-1][0] < temperatures[i]:
                stackT, stackInd = stack.pop()
                ret[stackInd]=i-stackInd

            stack.append((t, i))

        

        # # stack.append(temperatures[-1])

        # # for i in range(len(temperatures)-2, -1, -1):

        # #     temperatures[i]:
            
        # #     stack.append(temperatures[i])


    

        #  for i in range(len(temperatures)-1, -1, -1):
        #     stack.append(temperatures[i])



        # for temp in temperatures:
        #     stack.append(temp)

        return ret

        
        