class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        a &= MASK
        b &= MASK

        xorr = a ^ b
        an = (a & b) << 1
        while an !=0:
            temp = xorr & MASK
            xorr = xorr^an & MASK
            an = (temp & an) << 1 & MASK
        # return xorr
        return xorr if xorr <= MAX_INT else xorr - (1 << 32)