class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) 
        k = max(piles)

        while r > l:
            search = (l+r) // 2
            curr = 0
            for pile in piles:  
                curr += (pile + search -1) // search
            # print(search, curr)
            if(curr>h):
                l = search+1
            else:
                
                r = search
                k = min(k, search)
            
        return k
        