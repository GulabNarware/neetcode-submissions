class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        m=min(strs)

        for i in range(len(strs)):

            for j in range(len(m)):
                if m[j]!=strs[i][j]:
                    m=m[:j]
                    break

        return m