class MyQueue:

    def __init__(self):
        self.stack = list()
        self.helpstack = list()
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        if not self.stack: return False
        
        while self.stack:
            self.helpstack.append(self.stack.pop())
        res = self.helpstack.pop()
        while self.helpstack:
            self.stack.append(self.helpstack.pop())

        return res

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        if not self.stack: return True
        else: return False