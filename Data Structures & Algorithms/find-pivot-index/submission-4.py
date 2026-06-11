class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        p=[0]*(n+1)
        for i in range(1,n+1):
            p[i]=p[i-1]+nums[i-1]
        
        for j in range(n):
            leftsum=p[j]
            rightsum=p[-1]-p[j+1]
            if leftsum==rightsum:
                return j
        return -1
