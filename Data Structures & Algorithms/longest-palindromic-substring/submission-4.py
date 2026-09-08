class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        res = ""
        for i in range(len(s)):
            oddWord = s[i]
            left = i-1
            right = i+1
            oddResLen = 1
            oddRes=s[i]


            while left>=0 and right<len(s):
                if s[left] != s[right]:
                    break
                oddResLen+=2
                oddWord = s[left] + oddWord + s[right]
                oddRes=oddWord
                left-=1
                right+=1

            evenWord = ""
            evenResLen = 1
            left = i
            right = i+1
            evenRes=""

            while left>=0 and right<len(s):
                if s[left] != s[right]:
                    break
                evenResLen+=2
                evenWord = s[left] + evenWord + s[right]
                evenRes = evenWord
                left-=1
                right+=1
            
            # resLen = max(reslen, evenResLen, oddResLen)
            if evenResLen>resLen and evenResLen>oddResLen:
                resLen=evenResLen
                res=evenRes
            if oddResLen>=resLen and oddResLen>=evenResLen:
                resLen=oddResLen
                res=oddRes

        return res