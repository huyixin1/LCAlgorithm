class Solution:
    def __init__(self):
        self.res = []
        self.track = []
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack(1, n, k)
        return self.res
    def backtrack(self, start, n, k):
        # base case
        if k == len(self.track):
            self.res.append(list(self.track)) # ?why copy it
            return

        for i in range(start, n+1):
            self.track.append(i)
            self.backtrack(i+1, n, k)
            self.track.pop()
        