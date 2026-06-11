class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0
        s=set(nums)
        longest=0
        for i in s:
            if i-1 in s :
                length=1

                while (i+length) in s:
                    length+=1

                longest=max(length,longest)
        return longest+1



        