class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # ret = 0
        # stack = deque()
        # i = 0
        
        # while i < len(heights):

        #     height=heights[i]
            
        #     while i+1<len(heights):
        #         if heights[i+1] >= height:
        #             i+=1
        #             stack.append((i, height))
        #         elif stack:
        #             stack.popleft()
        #             break
                
            

        #     ret = max(stack[0[1]]*(stack[-1][0]-stack[0][0]+1), ret)
        #     i+=1
           

        # return ret
        


        maxArea = 0

        stack = [] # pair: (index, height)



        for i, h in enumerate(heights):

            start = i

            while stack and stack[-1][1] > h:

                index, height = stack.pop()
                
                maxArea = max(maxArea, height * (i - index))

                start = index

            stack. append ((start, h))



        for i, h in stack:

            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea