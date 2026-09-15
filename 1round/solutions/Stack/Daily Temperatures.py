class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic stack
        length = len(temperatures)
        s = []
        res = [0] * length
        for i in range(length-1, -1, -1):
            # iterate from back to front
            while s and temperatures[s[-1]] <= temperatures[i]:
                s.pop()
            res[i] = 0 if not s else s[-1] -i
            s.append(i) # add index not value

        return res

        