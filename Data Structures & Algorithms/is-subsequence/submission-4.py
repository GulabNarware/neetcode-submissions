class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # if len(s)==0 :
        #     return True
        # if len(t)==0:
        #     return False
        # s1=0
        # res=""
        # for i in range(len(t)):
        #     if s1<len(s) and t[i]==s[s1]:
        #         res+=t[i]
        #         s1+=1
        # if res==s:
        #     return True
        # else:
        #     return False



        c=0
        for ch in t:
            if c<len(s) and ch==s[c]:
                c+=1

        return True if c==len(s) else False