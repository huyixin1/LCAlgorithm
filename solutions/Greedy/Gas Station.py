class Solution:
    # by graph
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, min_sum, start = 0, 0, 0
        n = len(gas)

        for i in range(n):
            total += gas[i] - cost[i]
            if total < min_sum:
                # the next one is the lowest in the graph
                start = i + 1
                min_sum = total
        if total < 0: return -1
        return 0 if start == n else start # cycle array