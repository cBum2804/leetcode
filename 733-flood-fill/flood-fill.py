class Solution(object):
    def floodFill(self, image, sr, sc, color):
       
        rows, cols= len(image), len(image[0])
        initial_color = image[sr][sc]
        if image[sr][sc]==color:
            return image
        
        def get_neighbour(x,y):
          rowD = [-1,0,1,0]
          colD = [0,-1,0,1]

          for i in range(len(rowD)):
            neighbour_row = x+rowD[i]
            neighbour_col = y+colD[i] 
            if neighbour_row >=0 and neighbour_row< rows and neighbour_col>=0 and neighbour_col< cols:
                if image[neighbour_row][neighbour_col] == initial_color:
                    yield neighbour_row, neighbour_col

        def bfs(i, j):
            queue = deque()
            seen = set()
            queue.append((i,j))
            seen.add((i,j))
            image[i][j] = color

            while queue:
                current = queue.pop()

                for x,y in get_neighbour(current[0], current[1]):
                    if (x,y) not in seen:
                        seen.add((x,y))
                        queue.append((x,y))
                        image[x][y] = color
        bfs(sr,sc)
        return image