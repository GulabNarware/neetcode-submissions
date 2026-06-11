class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return False
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i-1]==nums[i]:
        #         return True

        # else:
        #     return False

        count={}
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                return True

        return False

        

        

