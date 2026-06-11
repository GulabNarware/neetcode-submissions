class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}

        for i in nums:
            count[i]=count.get(i,0)+1

        c=[]
        for i in range(k):
            a=0
            b=""
            for i in count:
                if a<count[i]:
                    a=count[i]
                    b=i
            c.append(int(b))
            count.pop(b)
        return c


