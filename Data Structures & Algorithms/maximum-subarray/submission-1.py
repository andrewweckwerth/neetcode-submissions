class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ma = float("-inf")
        curr = 0
        for i in range(len(nums)):
            curr+=nums[i]
            new = nums[i]
            curr = max(new, curr)
            ma=max(ma,curr)

        return ma if ma!=float("-inf") else 0

        #wow really easy i did this in 5 min
        