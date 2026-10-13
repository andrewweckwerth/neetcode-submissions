class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # di = {}
        # for num in nums:
        #     if num in di:
        #         return num
        #     di[num] = True
        # this one uses o(n) space

        # i = nums[0]
        # while nums[i] != -1:
        #     temp = nums[i]
        #     nums[i]=-1
        #     i=temp
        # return i
        # this one modifies the array
        
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
          
            
           
        slow_2=nums[0]
      
        while slow != slow_2:
            # if i%2:
            slow = nums[slow]
            slow_2 = nums[slow_2]
            # fast = nums[fast]
            

        print(slow, fast)

        return slow



        
        