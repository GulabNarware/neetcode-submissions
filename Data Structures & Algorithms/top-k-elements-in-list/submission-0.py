class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        
        l=[[]for j in range(len(nums)+1)]
        for n,c in d.items():
            l[c].append(n)
        
        res=[]
        for i in range(len(l)-1,0,-1):
            for n in l[i]:
                res.append(n)
                if len(res)==k:
                    return res

