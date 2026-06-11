class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indx={}

        for i in range(len(nums)):
            a=target-nums[i]
            if target-a not in indx:
                indx[a]=i

            else:
                return [indx[nums[i]],i]
