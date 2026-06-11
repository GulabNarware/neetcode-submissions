class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram={}
        for i in s:
            if i not in anagram:
                anagram[i]=1
            else:
                anagram[i]+=1

        for j in t:
            if j in anagram:
                anagram[j]-=1

            else:
                return False
        
        for i in anagram:
            if anagram[i]>0:
                return False

            if anagram[i]<0:
                return False
                

        return True
                
                