class Solution:
    # stack
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_stack(string):
            stack = []
            for s in string:
                if s != "#":
                    stack.append(s)
                elif stack:
                    stack.pop()
            return stack
        return process_stack(s) == process_stack(t)

class Solution:
    # two pointer
    def backspaceCompare(self, s: str, t: str) -> bool:
        def nextValidChar(str, index): # backwards since the well delete previous symbol
            backspace = 0
            while index >= 0:
                if backspace == 0 and str[index] != "#":
                    break
                elif str[index] == "#":
                    backspace += 1
                else: backspace -= 1
                index -= 1
            return index

        index_s, index_t = len(s)-1, len(t)-1
        while index_s >=0 or index_t >=0: # in case one of the string is out of boundary
            index_s = nextValidChar(s, index_s)
            index_t = nextValidChar(t, index_t)

            char_s = s[index_s] if index_s >= 0 else ""
            char_t = t[index_t] if index_t >= 0 else ""
        
            if char_s != char_t:
                return False

            index_s -= 1
            index_t -= 1
        return True
        