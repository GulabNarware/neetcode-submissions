class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        profit=0
        while right<len(prices):
            if prices[left]>prices[right]:
                left=right
                right+=1
            elif prices[left]<=prices[right]:
                add=prices[right]-prices[left]
                right+=1
                if add>profit:
                    profit=add
        return profit