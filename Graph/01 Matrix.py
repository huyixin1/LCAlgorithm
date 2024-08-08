class Solution:
    # BFS
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        res = [[-1 for _ in range(n)] for _ in range(m)] # to mark not visited

        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append((i,j))
                    res[i][j] = 0

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                next_x, next_y = x + dx, y + dy
                if 0 <= next_x < m and 0 <= next_y < n and res[next_x][next_y] == -1: # include boundar
                    q.append((next_x, next_y))
                    res[next_x][next_y] = res[x][y] + 1

        return res