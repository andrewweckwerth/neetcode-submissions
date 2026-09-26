class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c]=='.':
                    continue

                #
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3) * 3 + (c // 3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3) * 3 + (c // 3)].add(board[r][c])
        # for r in range(len(board)):
            


        #     for c in range(len(board[0])):
                
        #         seen = set()
        #         if board[r][c]=='.':
        #             continue
        #         if board[r][c] in seen:
        #             return False
        #         seen.add(board[r][c])

        #     for c in range(len(board[0])):
                
        #         for r in range(len(board)):
                    
        #             seen = set()
        #             if board[r][c]=='.':
        #                 continue
        #             if board[r][c] in seen:
        #                 return False
        #             seen.add(board[r][c])    


        # for r in range 



        return True
        