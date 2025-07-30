class Solution(object):
    def mergeAlternately(self, word1, word2):
        output = ""
        w1 = 0
        while w1< len(word1) or w1< len(word2) :
            if w1< len(word1):
                output+=word1[w1]
            if w1< len(word2):
                output+=word2[w1]
            w1+=1

        return output
        