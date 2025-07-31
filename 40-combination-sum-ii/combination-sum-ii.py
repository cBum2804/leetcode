class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def search(i, curr, total):
            if total==target:
                res.append(curr[:])
                return
            if total > target or i==len(candidates):
                return
            curr.append(candidates[i])
            search(i+1,curr, total + candidates[i]) 
            curr.pop()      
            while i+1< len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            search(i+1, curr, total)
        search(0,[],0)
        return res