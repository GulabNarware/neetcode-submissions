class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        mxP=0

        while r< len(prices):

            if prices[l]< prices[r]:

                total=prices[r]-prices[l]

                mxP=max(total,mxP)

            else:
                l=r
            r+=1

        return mxP