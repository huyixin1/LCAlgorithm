class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        num = 0
        stack = [] # stack for store
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == "[":
                # store num before
                stack.append(num)
                stack.append(res)
                num = 0 # reset
                res = ""

            elif c == "]":
                preres = stack.pop()
                prenum = stack.pop()
                res = preres + prenum * res

            else:
                res += c # string

        return res
