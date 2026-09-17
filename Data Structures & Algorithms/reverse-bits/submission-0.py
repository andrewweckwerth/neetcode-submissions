class Solution:
    def reverseBits(self, n: int) -> int:
        
        ret = 0
        for i in range(32):
            temp=(n >> i) & 1
            ret = ret | (temp << (31-i))
        return ret