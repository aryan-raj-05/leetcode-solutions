class MinStack:
    def __init__(self):
        self.stack = []
        self.min_values = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_values) == 0:
            self.min_values.append(val)
            return
        self.min_values.append(min(self.min_values[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_values.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]
