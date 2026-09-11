class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '([{': #c is opening bracket
                stack.append(c)
            else: #c is closing bracket
                if not stack or \
                    (c == ')' and stack[-1] != '(') or\
                    (c == ']' and stack[-1] != '[') or\
                    (c == '}' and stack[-1] != '{'):
                    return False
                stack.pop()
        return not stack # if stack is empty then it is valid