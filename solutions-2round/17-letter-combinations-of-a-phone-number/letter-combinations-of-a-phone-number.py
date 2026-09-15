class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {
                    '2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz'
                }
        res = []
        path = []
        def dfs(start):
            if len(path) == len(digits): # logically won't out of index
                res.append("".join(path))
                return
            for letter in dic[digits[start]]:
                path.append(letter)
                dfs(start+1)
                path.pop()

        dfs(0)
        return res