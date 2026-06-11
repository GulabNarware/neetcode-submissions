class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left =1
        right =max(piles)
        k=right
        while left <= right:
            mid=(left + right)//2
            hours=0
            for i in piles:
                hours+=math.ceil(float(i)/mid)
            
            if hours<=h:
                right=mid-1
                
                k=mid
            else:
                left=mid+1
        return k