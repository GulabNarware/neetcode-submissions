class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:return [nums]
        result=[]
        s=set()
        used=[False]*len(nums)
        def comb(sub):
            if len(sub)==len(nums):
                if tuple(sub) not in s:
                    s.add(tuple(sub))
                    result.append(sub.copy())
                return 
    
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i]=True
                sub.append(nums[i])
                comb(sub)
                sub.pop()
                used[i]=False

        comb([])
        return result