
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.ma = []

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.ma:
            self.ma.append(val)
        else:
            self.ma.append(min(val, self.ma[-1]))

        

    def pop(self) -> None:
        self.stack.pop()
        self.ma.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.ma[-1]

        
