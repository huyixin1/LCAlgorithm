class Solution:
    # BFS
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # the shortest path length from 2 to all 1
        step = self.BFS(grid)
        return step

    def BFS(self, grid):
        q = deque()
        step = 0
        r = len(grid)
        c = len(grid[0])
        for i in range(r): # add rotten
            for j in range(c):
                if grid[i][j] == 2:
                    q.append((i,j)) # tuple
        
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            sz = len(q) # add nodes by layers
            for i in range(sz):
                x, y = q.popleft()
                for dx, dy in dirs:
                    next_x, next_y = x + dx, y + dy
                    if 0 <= next_x < r and 0 <= next_y < c and grid[next_x][next_y] == 1:
                        grid[next_x][next_y] = 2
                        q.append((next_x, next_y))
            step += 1
        # detect if there is left fresh orange
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    return -1
        return sstep if step == 0 else step-1