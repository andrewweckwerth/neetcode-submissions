class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        di = {}
        for num in nums:
            if num in di:
                return num
            di[num] = True
        
        