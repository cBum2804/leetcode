class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh_count=0
        EMPTY, FRESH, ROTTEN = 0,1,2
        row,col = len(grid), len(grid[0])
        seen = set()

        for i in range(row):
            for j in range(col):
                if grid[i][j]==ROTTEN:
                    q.append((i,j))
        
                elif grid[i][j] == FRESH:
                    fresh_count +=1

        if fresh_count==0:
            return 0
        num_minutes=-1
        while q:
            num_minutes+=1
            q_size = len(q)

            for _ in range(q_size):
                i, j = q.popleft()
                for r,c in [(i,j+1),(i,j-1),(i+1, j),(i-1,j)]:
                    if r>=0 and r< row and c>=0 and c< col and grid[r][c]== FRESH and (r,c)not in seen:
                        q.append((r,c))
                        seen.add((r,c))
                        fresh_count-=1
                        grid[r][c]= ROTTEN
        if fresh_count==0:
            return num_minutes
        else:
            return -1

