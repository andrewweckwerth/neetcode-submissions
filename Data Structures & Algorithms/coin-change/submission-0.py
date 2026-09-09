class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        memo[0]=0

        def dfs(i):

            for coin in coins:
                if i-coin in memo and memo[i-coin]!=-1:
                    if i not in memo:
                        memo[i]= memo[i-coin] + 1
                    else:
                        memo[i]= min(memo[i-coin] + 1, memo[i])
            if i not in memo:
                memo[i]=-1
            print(i, amount)
            if i==amount:
                
                return memo[i]
            return dfs(i+1)


        return dfs(0)

