class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        path = []
        def dfs(start):
            s = 0
            for i in path:
                s += i
            if s > target: # invalid choice
                return
            if s == target: 
                res.append(path[:])
                return

            for start in range(len(candidates)):
                if candidates[start] <= target:
                    path.append(candidates[start])
                    dfs(start)
                    path.pop()

        dfs(0)
        # ① 对每个内部列表排序，再转元组
        tuples = [tuple(sorted(x)) for x in res]

        # ② 用 set 去重
        unique_tuples = set(tuples)

        # ③ 转回列表
        unique_lists = [list(t) for t in unique_tuples]
        return unique_lists