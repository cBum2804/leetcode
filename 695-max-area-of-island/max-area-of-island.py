class Solution(object):
    def maxAreaOfIsland(self, grid):
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        def dfs(x,y):
            if(x<0 or x>=rows or y<0 or y>= cols or grid[x][y]!=1):
                return 0
            else:
                grid[x][y] = 0
                return 1 + dfs(x+1,y) + dfs(x-1,y) + dfs(x,y+1) + dfs(x,y-1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i,j))
        return max_area
        