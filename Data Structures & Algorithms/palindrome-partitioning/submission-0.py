class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result=[]

        def rec(indx,sub):

            if indx>=len(s):
                result.append(sub.copy())
                return 
            for i in range(indx,len(s)):
                temp=s[indx:i+1]
                if temp==temp[::-1]:
                    sub.append(temp)
                    rec(i+1,sub)
                    sub.pop()

        rec(0,[])
    
        return result

                
