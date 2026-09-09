class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        maxPro = nums[0]
        minPro = nums[0]
        for i in range(len(nums)):
            if i == 0:
                continue


            prevMax = currMax
            prevMin = currMin

            currMax = max(nums[i], nums[i]* prevMax, nums[i]* prevMin)
            currMin = min(nums[i], nums[i]* prevMax, nums[i]* prevMin)
            minPro = min(minPro, currMin)
            maxPro = max(maxPro, currMax)




            # currMax = max(nums[i], nums[i]* currMax, nums[i]* currProMin)
            # currProMin = min(nums[i], nums[i]* currProMin)
            # minPro = min(minPro, currProMin)
            # maxPro = max(maxPro, currMax)
        return maxPro
            

