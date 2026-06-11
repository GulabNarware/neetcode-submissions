class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # c=0
        # for i in nums:
        #     if i==val:
        #         c+=1
        # index=0
        # while c>0:
        #     if nums[index]==val:
        #         nums.pop(index)
        #         c-=1
        #         if index!=0:
        #             index-=1

        #     else:
        #         index+=1

        # return len(nums)

        k=0

        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1

        return k

        
            


            