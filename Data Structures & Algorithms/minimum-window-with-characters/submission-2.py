class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        
        countT,window={},{}

        for i in t:
            countT[i]=1+countT.get(i,0)
        
        left=0
        resln=float("inf")
        result=[-1,-1]
        have,need=0,len(countT)


        for right in range(len(s)):
            c=s[right]
            window[c]=1+window.get(c,0)

            if c in countT and countT[c]==window[c]:
                have+=1
            
            while have==need:
                if right-left+1<resln:
                    result=[left,right]
                    resln=right-left+1

                window[s[left]]-=1

                if s[left] in countT and window[s[left]]<countT[s[left]]:
                    # window[s[left]]-=1
                    have-=1
                left+=1
        left,right=result
        

        return s[left:right+1] if resln!=float("inf") else ""  





            
