class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        bracket=[""]*(n*2)

        def backtrack(indx,total):
            if indx>=len(bracket):
                if total==0:
                    result.append("".join(bracket))

                return 


            if total<0:
                return 

            if total>len(bracket)//2:
                return 

            bracket[indx]="("
            s=total+1

            backtrack(indx+1,s)

            bracket[indx]=")"

            s=total-1

            backtrack(indx+1,s)

        backtrack(0,0)

        return result
        