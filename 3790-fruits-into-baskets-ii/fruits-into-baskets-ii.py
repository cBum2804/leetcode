class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        output = 0
        for fruit in fruits:
            unplaced = 1
            for i in range(len(baskets)):
                if fruit <= baskets[i]:
                    unplaced = 0
                    baskets[i]=0
                    break
            output+=unplaced
        return output