class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word=""
        smol=min(len(word1),len(word2))
        for i in range(smol):
            word+=word1[i]+word2[i]

        if(len(word1)>len(word2)):
            word+=word1[smol:]
        else:
            word+=word2[smol:]
        return word
        

        