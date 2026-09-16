class MinStack:

    def __init__(self):
        self.stk = []
        self.minStk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        # keep the top of Minstk is the smallest
        if not self.minStk or val <= self.minStk[-1]:
            self.minStk.append(val)
            

    def pop(self) -> None:
        if self.stk[-1] == self.minStk[-1]: # top is the smallest
            self.minStk.pop()
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minStk[-1]
        