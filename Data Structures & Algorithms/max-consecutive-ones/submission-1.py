class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        old=-1
        greatest=0
        for i in nums:
            if i ==1:
                c+=1
            else:
                old=max(c,old)
                c=0
        else:
            greatest=max(c,old)
        return greatest
