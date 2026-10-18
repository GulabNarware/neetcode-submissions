class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]

        def back(indx,sub):
            if indx>=len(nums):
                result.append(sub.copy())

                return 


            sub.append(nums[indx])
            back(indx+1,sub)
            sub.pop()
            back(indx+1,sub)
        back(0,[])
        return result