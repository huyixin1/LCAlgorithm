class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for token in tokens:
            if token in "+-*/":
                a = res.pop()
                b = res.pop()
                if token == '+':
                    res.append(a+b)
                elif token == '*':
                    res.append(a*b)
                elif token == '-':
                    res.append(b-a)
                elif token == '/':
                    res.append(int(b/a))
            else:
                res.append(int(token))

        return res.pop()