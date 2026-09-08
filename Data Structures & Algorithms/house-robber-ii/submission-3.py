class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        i = 0
        first = False

        def dfs(i, first):
            if i==0:
                ne, first1 = dfs(i+1, first)
                skip, first2 = dfs(i+2, True)
                skip +=nums[i]
                if(ne>=skip):
                    key = (0, first1)
                    memo[key]=ne
                    return ne, first1
                if(skip>ne):
                    key = (0, True)
                    memo[key]=skip
                    return skip, True


            if first and i == len(nums)-1:
                return 0, first

            if i > len(nums)-1:
                return 0, first
            
            if (i, first) in memo:
                return memo[(i, first)]
            ne, first1 = dfs(i+1, first)
            skip, first2 = dfs(i+2, first)
            skip += nums[i]
            if(ne>=skip):
                memo[(i,first1)]=[ne, first1]
                return ne, first1
            if(skip>ne):
                memo[(i,first2)]=[skip, first2]
                return skip, first2
        ma, first = dfs(i, first)
        return ma



