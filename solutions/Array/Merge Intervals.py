class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0]) # increasing sort based on first ele
        res.append(intervals[0])
        for curr in intervals[1:]:
            # overlapping
            last = res[-1]
            if last[1] >= curr[0]: 
                #renew the overlapping interval
                last[1] = max(last[1], curr[1])
            else:
                res.append(curr) # next waited to merge interval
        return res