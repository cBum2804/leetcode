class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col = len(grid), len(grid[0])
        EMPTY, FRESH, ROTTEN = 0,1,2
        fresh_count=0
        q = deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == FRESH:
                    fresh_count+=1
                elif grid[i][j] == ROTTEN:
                    q.append((i,j))

        if fresh_count ==0:
            return 0
        minutes = -1
        while q:
            len_q = len(q)
            minutes+=1
            for _ in range(len_q):
                x, y = q.popleft()
                for r,c in [(x,y+1),(x,y-1),(x+1,y),(x-1,y)]:
                    if r>=0 and r<row and c>=0 and c<col and grid[r][c]== FRESH:
                        grid[r][c]= ROTTEN
                        q.append((r,c))
                        fresh_count-=1
        if fresh_count == 0:
            return minutes
        else:
            return -1
        