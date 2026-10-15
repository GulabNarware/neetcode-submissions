class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]
        def back(indx,total,sub):

            if indx>=len(candidates):
                if total==target:
                    result.append(sub.copy())
                return 

            if total>target:
                return 

            if total==target:
                result.append(sub.copy())
                return 

            sm=total+candidates[indx]

            sub.append(candidates[indx])
            
            back(indx+1,sm,sub)

            sub.pop()

            #duplicate skipp kar rahe h 
            indx+=1
            while indx<len(candidates) and candidates[indx-1] == candidates[indx]:
                indx+=1

            back(indx,total,sub)
            


        back(0,0,[])

        return result

