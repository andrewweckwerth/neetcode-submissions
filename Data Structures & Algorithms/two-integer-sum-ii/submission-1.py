class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ret = [0,0]
        left = 0
        right = len(numbers)-1

        while numbers[left]+numbers[right]!= target:
            
            if(numbers[left]+numbers[right]< target):
                left+=1
            else:
                right-=1
        return [left+1, right+1]
        