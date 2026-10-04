class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # left = (0,0)
        # right = (len(matrix), len(matrix[0]))
        left = 0
        right = len(matrix)*len(matrix[0])
        while left!=right:
            search = (left+right)//2
            #print(search)


            row = search // len(matrix[0])
            col = (search - row*len(matrix[0]))
            #print(row, col)

            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                left = search+1
            if matrix[row][col] > target:
                right = search
        return False
        