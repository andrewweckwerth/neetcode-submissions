class Solution:
    def trap(self, height: List[int]) -> int:
        
        # total= 0
        # left = 0
        # right = 2

        leftMax = [0 for _ in range(len(height))]
        rightMax = [0 for _ in range(len(height))]
        
        total = 0
        

        # while right<len(height) and left<len(height)-1:

        for i in range(1, len(height), 1):
            
            leftMax[i] = max(leftMax[i-1], height[i-1])
        
        for i in range(len(height)-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i+1])
            
            
        # print(leftMax)
        # print(rightMax)



        for i in range(1, len(height), 1):
            mi = min(leftMax[i], rightMax[i])
            su = mi-height[i] 
            total+= max(0,su)



        return total

        