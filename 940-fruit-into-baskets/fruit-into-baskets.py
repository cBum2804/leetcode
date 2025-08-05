class Solution(object):
    def totalFruit(self, fruits):
        start = 0
        fruit_count = defaultdict(int)
        output = 0

        for i in range(len(fruits)):
            fruit_count[fruits[i]] +=1

            while len(fruit_count) > 2:
                fruit_count[fruits[start]] -=1
                if fruit_count[fruits[start]]==0:
                    del fruit_count[fruits[start]]
                start+=1

            output = max(output, i-start+1)
        
        return output