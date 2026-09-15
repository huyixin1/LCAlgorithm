class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        path = []
        def dfs(left, right):
            if left == n and right == n:
                res.append(''.join(path))
                return

            # equal to 
            # choices = ['(', ')']
            # for ch in choices:
            if left < n:
                path.append('(')
                dfs(left+1, right)
                path.pop()

            if right < left:
                path.append(')')
                dfs(left, right+1)
                path.pop()

        dfs(0,0)
        return res