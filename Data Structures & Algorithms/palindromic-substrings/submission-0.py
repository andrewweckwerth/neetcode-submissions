class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            print(s[i])
            count+=1
            left=i-1
            right=i+1
            while left>=0 and right<len(s):
                if s[left]!=s[right]:
                    break
                count+=1
                left-=1
                right+=1
            left=i
            right=i+1
            while left>=0 and right<len(s):
                if s[left]!=s[right]:
                    break
                count+=1
                left-=1
                right+=1
            
        return count