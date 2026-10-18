class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.result=[]

        def back(indx,comb):

            if indx>=len(nums):
                self.result.append(nums[:indx])
                return 

            # comb.append(nums[indx])

            for i in range(indx,len(nums)):

                #exploire

                nums[i],nums[indx]=nums[indx],nums[i]


                #search
                back(indx+1,comb)
               


                #backtrack

                nums[i],nums[indx]=nums[indx],nums[i]

        back(0,[])

        return self.result