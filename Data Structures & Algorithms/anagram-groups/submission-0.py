class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # output=[]

        # for i in strs:
        #     sublist=[]
        #     for j in strs:

        #         if len(i)!=len(j):
        #             continue

        #         count={}

        #         for k in i:
        #             if k not in count:
        #                 count[k]=1
        #             else:
        #                 count[k]+=1

        #         for h in j:
        #             if h in count:
        #                 count[h]-=1
        #             else:
        #                 count[h]=1
        #         is_ang=True
        #         for f in count:
        #             if count[f]>0 or count[f]<0:
        #                 is_ang=False
        #         if is_ang:
        #             sublist.append(j)
                    

        #     output.append(sublist)

        # return output
                    
        groups={}

        for word in strs:
            key ="".join(sorted(word))
            if key not in groups:
                groups[key]=[]

            groups[key].append(word)

        return list(groups.values())



