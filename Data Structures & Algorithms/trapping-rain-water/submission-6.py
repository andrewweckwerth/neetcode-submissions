class Solution:
    def trap(self, height: List[int]) -> int:
        
        # leftMax = [0 for _ in range(len(height))]
        # rightMax = [0 for _ in range(len(height))]
        
        # total = 0
        
        # for i in range(1, len(height), 1):
            
        #     leftMax[i] = max(leftMax[i-1], height[i-1])
        
        # for i in range(len(height)-2, -1, -1):
        #     rightMax[i] = max(rightMax[i+1], height[i+1])
            
        # for i in range(1, len(height), 1):
        #     mi = min(leftMax[i], rightMax[i])
        #     su = mi-height[i] 
        #     total+= max(0,su)

        # return total

        #o(n) solution and o(n) memory solution above
        #o(n) solution and o(1) memory solution below

        left = 0
        right = len(height)-1
        leftMax = 0
        rightMax = 0
        total=0

        while not (left > right):

          
            
            if height[right]<height[left]:
                
                
                rightMax = max(rightMax,height[right])
                mi = min(leftMax, rightMax)
                
                
                
                total+= max(0,rightMax-height[right] )
                # print("right", total)
                right-=1
                


            else:
                
                leftMax = max(leftMax,height[left])
              
                total+= max(0,leftMax-height[left])
                # print("left", total)
                left+=1
                
        
        return total


        

        