class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def rec(i, bought):
            if i == len(prices):
                return 0
            if (i, bought) in dp:
                return dp[(i, bought)]
            result = rec(i+1, bought)
            if bought:
                result = max(result, prices[i] + rec(i+1, False))
            else:
                result = max(result, -prices[i] + rec(i+1, True))        
            dp[(i,bought)] = result
            return result

        return rec(0, False)        