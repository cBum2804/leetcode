class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        x=0
        while x < len(word1) or x < len(word2):
            if x < len(word1):
                result.append(word1[x])
            if x < len(word2):
                result.append(word2[x])
            x+=1
        
        return "".join(result)
            

        