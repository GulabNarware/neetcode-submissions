class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq={}
        for i in range(len(s1)):
            freq[s1[i]]=1+freq.get(s1[i],0)

        ln=len(freq)
        for i in range(len(s2)):
            freq2,curr={},0
            for j in range(i,len(s2)):
                freq2[s2[j]]=1+freq2.get(s2[j],0)
                if freq2[s2[j]] > freq.get(s2[j],0):
                    break
                if freq.get(s2[j],0)==freq2[s2[j]]:                    
                    curr+=1
                if curr==ln:
                    return True
        return False

        