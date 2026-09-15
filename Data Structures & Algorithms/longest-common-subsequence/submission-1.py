class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo=[[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        
        def dfs(i, j):

            if(i>len(text1)-1):
                return 0

            if(j>len(text2)-1):
                return 0
            if memo[i][j]!=-1:
                return memo[i][j]
            if text1[i]==text2[j]:
                memo[i][j] = dfs(i+1, j+1) +1
                return memo[i][j]

            else:
                memo[i][j] = max( dfs(i+1, j), dfs(i, j+1))
                return memo[i][j]
                # return dfs(i+1, j) and dfs(i, j+1)
        

        return dfs(0,0)