class Solution(object):
    def floodFill(self, image, sr, sc, color):
       
        rows,cols = len(image), len(image[0])
        def neighbours(row,col, initial_color):
            rowD = [-1,0,1,0]
            colD = [0,-1,0,1]

            for x in range(len(colD)):
                neighbour_row = row+rowD[x]
                neighbour_col = col+colD[x]

                if neighbour_row>=0 and neighbour_row < rows and neighbour_col>=0 and neighbour_col< cols:
                    if image[neighbour_row][neighbour_col]== initial_color:
                        yield neighbour_row, neighbour_col
        def bfs(sr, sc):
            queue = deque()
            queue.append((sr,sc))
            seen = set()
            seen.add((sr,sc))
            initial_color = image[sr][sc]
            image[sr][sc] = color

            while queue:
                current = queue.popleft()
                for i,j in neighbours(current[0],current[1],initial_color):
                    if (i,j) not in seen:
                        seen.add((i,j))
                        queue.append((i,j))
                        image[i][j] = color
        bfs(sr, sc)
        return image        

