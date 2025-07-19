class Solution(object):
    def groupAnagrams(self, strs):
        mapResult = defaultdict(list)

        for word in strs:
            sortedWord = ''.join(sorted(word))
            mapResult[sortedWord].append(word)
        return list(mapResult.values())
        