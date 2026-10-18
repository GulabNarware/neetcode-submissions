class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        s=set()

        # result=[]
        # def back(indx,comb):

        #     if indx>=len(nums):
        #         if tuple(comb) not in s:
        #             result.append(comb.copy())
        #             s.add(tuple(comb))
        #         return 

        #     comb.append(nums[indx])

        #     back(indx+1,comb)
        #     comb.pop()
        #     back(indx+1,comb)

        # back(0,[])

        # return result


        nums.sort()
        result=[]
        def back(indx,comb):

            if indx>=len(nums):
                result.append(comb.copy())
                return 

            comb.append(nums[indx])

            back(indx+1,comb)

            comb.pop()

            while indx+1 < len(nums) and nums[indx]==nums[indx+1]:
                indx+=1

            back(indx+1,comb)

        back(0,[])
        return result
            