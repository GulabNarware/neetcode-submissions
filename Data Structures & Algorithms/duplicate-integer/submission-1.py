class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

            if d[i]==2:
                return True
        return False 
