class Solution(object):
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        
        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]!='1':
                return 
            else:
                grid[i][j] = '0'
                dfs(i,j+1)
                dfs(i,j-1)
                dfs(i-1,j)
                dfs(i+1,j)

        number_of_island = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    number_of_island +=1
                    dfs(i, j)
                    
        return number_of_island