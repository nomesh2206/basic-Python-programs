class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        op = ""
        for i in range(max(len(word1), len(word2))):
            if i<len(word1):
                op+= word1[i]
            if i<len(word2):
                op+= word2[i]
        return op
