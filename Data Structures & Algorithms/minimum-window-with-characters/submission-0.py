class Solution:
    def minWindow(self, s: str, t: str) -> str:

        window, countT = {}, {}

        res, resLen = [-1,-1], float("inf")

        for c in t:
            countT[c] = 1 + countT.get(c,0)
        print(countT)

        have=0
        need=len(countT)
        l=0
        for r in range(len(s)):
            c = s[r]
            window[c]=1+window.get(c,0)

            if c in countT and window[c]==countT[c]:
                have+=1

            while have==need:
                if resLen>r-l+1:
                    res=[l,r]
                    resLen=r-l+1
                
                
                c = s[l]
                window[c]-=1

                if c in countT and window[c]<countT[c]:
                    have-=1
                l+=1

        return s[res[0]:res[1]+1]


        