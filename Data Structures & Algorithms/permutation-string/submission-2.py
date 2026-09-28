class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        s1_hash = {}
        s2_hash = {}

        for c in s1:

            s1_hash[c]= s1_hash.get(c,0)+1
        print(s1_hash)

        for i in range(len(s1)):
            s2_hash[s2[i]]= s2_hash.get(s2[i],0)+1

        if s2_hash == s1_hash:
                return True

        for i in range(len(s1), len(s2)):
            print(s2_hash)
            
            s2_hash[s2[i]]= s2_hash.get(s2[i],0)+1
            s2_hash[s2[i-len(s1)]]= s2_hash.get(s2[i-len(s1)],0)-1
            if s2_hash[s2[i-len(s1)]]==0:
                s2_hash.pop(s2[i-len(s1)])
            if s2_hash == s1_hash:
                return True


        return False

        