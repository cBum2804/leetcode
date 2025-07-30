class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        output = []
        maxCandies = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                output.append(True)
            else:
                output.append(False)
            
        return output