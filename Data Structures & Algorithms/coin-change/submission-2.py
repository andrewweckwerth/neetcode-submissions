class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        memo[0]=0

        def recurse(i):

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

            #i implemented this as a recursive function with i+1 which is pretty much just a for loop lol
            return recurse(i+1)


        return recurse(0)

