class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=0

        while right < len(nums):

            if nums[left]==0 and nums[right]>0:
                temp=nums[left]

                nums[left]=nums[right]
                nums[right]=temp

                right+=1
                left+=1

            elif nums[left]!=0 :
                left+=1
                right=left

            elif nums[right]<1:
                right+=1
        return nums


            

