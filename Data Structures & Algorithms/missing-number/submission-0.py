class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [-1]*(len(nums)+1)
        for i in range(len(nums)):
            arr[nums[i]]=1
            print(nums[i])
        print(arr)
        for i in range(len(arr)):
            if(arr[i])==-1:
                return i

        return 0


        