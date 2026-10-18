class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        l=[i for i in range(1,n+1)]


        self.result=[]

        def back(indx,comb):
            if indx>=len(l):
                if len(comb)==k:
                    self.result.append(comb.copy())

                return 


            if len(comb)==k:
                self.result.append(comb.copy())

                return 


            comb.append(l[indx])

            back(indx+1,comb)
            comb.pop()
            back(indx+1,comb)

        back(0,[])
        return self.result