class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        s = []

        for i in range(n-1, -1, -1): # iterate backwards
            while s and temperatures[i] >= temperatures[s[-1]]:
                s.pop() # remove element from top of stack if they are smaller
            
            res[i] = 0 if not s else s[-1]-i
            s.append(i) # store index
        return res

        