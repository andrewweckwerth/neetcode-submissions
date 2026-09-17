class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [i for i in range(n+1)]
        for i in range(len(arr)):
            count=0
            num=arr[i]
            while num!=0:
                if(num%2==1):
                    count+=1
                num=num//2
            arr[i]=count
            
        return arr