class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = [[-1 for _ in range(n)] for _ in range(m)]


        def dfs(x,y):

            if x== n - 1 and y == m - 1:
                return 1

            if x >= n or y >= m:
                return 0

            if memo[y][x] != -1:
                return memo[y][x]

            memo[y][x] = dfs(x + 1, y) + dfs(x, y + 1)
            return memo[y][x]

        return dfs(0, 0)
            
            # if y==m-1 and x == n-1:
            #     return 1
            # if n>=x and m>=y:
            #     return dfs(x+1, y) + dfs(x,y+1)
            # elif n>=x:
            #      return dfs(x+1, y)
            # elif m>=y:
            #     return dfs(x,y+1)
            # return 0
        return dfs(0,0)