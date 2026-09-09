class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        li = [""] * (len(s)+1)
        
        for i in range(1,len(s)+1):
            for word in wordDict:
                if len(word)>i:
                    continue
                # print(s[i-len(word):i])
                if(s[i-len(word):i]==word and li[i - len(word)] == s[:i - len(word)]):
                    print("here")
                    print(i)
                    li[i]=li[i-len(word)]+word
        print(li)
        if li[len(s)]==s:
            return True
        return False