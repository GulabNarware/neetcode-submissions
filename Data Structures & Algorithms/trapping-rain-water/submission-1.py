class Solution:
    def trap(self, height: List[int]) -> int:
        
        prefix=[0]*(len(height))

        suffix=[0]*(len(height))

        for i in range(len(height)):
            if i==0:
                prefix[0]=height[0]

            else:
                prefix[i]=max(prefix[i-1],height[i])

        for j in range(len(height)-1,-1,-1):
            if j==len(height)-1:
                suffix[j]=height[j]

            else:
                suffix[j]=max(height[j],suffix[j+1])

        res=0
        for i in range(len(height)):
            res+=min(prefix[i],suffix[i])-height[i]

        

        return res