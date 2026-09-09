class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        li=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    li[i]=max(li[i], li[j]+1)
        return max(li)
        