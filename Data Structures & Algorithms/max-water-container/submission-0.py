class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        area=0
        while left<right:
            h=min(heights[left],heights[right])
            d=right-left

            a=h*d
            if area<a:
                area=a
            
            if heights[left]<heights[right]:
                left+=1
            elif heights[left]>heights[right]:
                right-=1
            else:
                left+=1
                right-=1
        return area