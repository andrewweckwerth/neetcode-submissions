class Solution:
    def canJump(self, nums: List[int]) -> bool:

        valid = set()
        valid.add(len(nums)-1)
        for i in range(len(nums)-1,-1,-1):
        
            for j in range(nums[i]+1):
                # print("i", i, "j", j)
                if i + j in valid:
                    valid.add(i)
        # print(valid)
        if 0 in valid:
            return True
        return False

        
        
        # while i<len(nums):
        #     print(i)
             
            
        #     if i == len(nums)-1 :
        #         return True 
        #     #print(i)
        #     if nums[i] == 0:
               
        #         print(i)
        #         print("here")
        #         print(len(nums)-1)
        #         return False
        #     # i+=nums[i]
        #     i+=nums[i]
    
        #     # if i == len(nums)-1 :
        #     #     return True 
        return False
        