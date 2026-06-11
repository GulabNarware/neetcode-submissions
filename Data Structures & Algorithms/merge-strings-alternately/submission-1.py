class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # res=""
        # if len(word1)< len(word2):
        #     for i in range(len(word1)):
        #         res+=word1[i]+word2[i]
        #     else:
        #         res+=word2[i+1:]
        # else:
        #     for i in range(len(word2)):
        #         res+=word1[i]+word2[i]
        #     else:
        #         res+=word1[i+1:]  

        # return res              

        n, m = len(word1), len(word2)
        res = []
        for i in range(max(m, n)):
            if i < n:
                res.append(word1[i])
            if i < m:
                res.append(word2[i])
        return "".join(res) 