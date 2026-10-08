class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = (len(nums1)+ len(nums2))
        part_len = total//2
        
        A, B = nums1, nums2

        if(len(A)>len(B)):
            A, B = B, A

        l, r = 0, len(A)-1

        while True:
            part_1 = (l+r)//2
            part_2 = part_len-part_1 -2

            Al = A[part_1] if part_1 >=0 else float("-inf")
            Ar = A[part_1+1] if part_1 + 1< len(A) else float("inf")
            Bl = B[part_2] if part_2 >=0 else float("-inf")
            # print(part_len)
            # print(part_1)
            # print(part_2)
            Br = B[part_2+1] if (part_2 + 1 < len(B))else float("inf")


            if (Al<=Br and Bl<= Ar):
                
                if total % 2 == 1:
                    return min(Ar, Br)
                else:
                    return (max(Al, Bl)+ min(Ar, Br))/2
            elif Al>Br:
                r = part_1-1
            else:
                l = part_1+1


            

            # if(nums[part_1]>nums[part_2+1]):
            #     r = search-1
            # if(nums[part_2]>nums[part_1+1]):
            #     l = search-1

        return 0
        