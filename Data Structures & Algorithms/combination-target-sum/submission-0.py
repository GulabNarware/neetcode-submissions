class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result=[]

        def back(indx,total,sub):
            if indx>=len(nums):
                if total==target:
                    result.append(sub.copy())

                return 

            if total==target:
                result.append(sub.copy())

                return 

            if total>target:
                return 


            sm=total+nums[indx]

            sub.append(nums[indx])

            back(indx,sm,sub)

            sub.pop()

            back(indx+1,total,sub)


        back(0,0,[])

        return result