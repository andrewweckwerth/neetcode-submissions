class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # di = {}
        # for num in nums:
        #     if num in di:
        #         return num
        #     di[num] = True
        # this one uses o(n) space

        i = nums[0]
        while nums[i] != -1:
            temp = nums[i]
            nums[i]=-1
            i=temp
        return i
        
        