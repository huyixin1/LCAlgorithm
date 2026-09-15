class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort() # pre cut the tree
        res = []
        path = []
        def dfs(start, remain):
            # s = 0
            # for i in path:
            #     s += i
            # calculate sum everytime, better to keep it as a parameter pass with the func
            if remain == 0: 
                res.append(path[:])
                return

            for i in range(start, len(candidates)): # only choose the nums next
                if candidates[i] > remain: break
                if candidates[i] <= target:
                    path.append(candidates[i])
                    dfs(i, remain - candidates[i])
                    path.pop()

        dfs(0, target)
        return res