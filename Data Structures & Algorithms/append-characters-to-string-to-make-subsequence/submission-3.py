class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        count=len(t)
        sp=0
        for i in range(len(s)):

            if sp < len(t) and s[i]==t[sp]:
                count-=1
                sp+=1

        return count