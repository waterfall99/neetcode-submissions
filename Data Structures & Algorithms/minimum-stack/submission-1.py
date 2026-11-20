class MinStack:

    def __init__(self):
        self.Min_Stack = []

    def push(self, val: int) -> None:
        if not self.Min_Stack:
            current_min = val
        else:
            current_min = min(val, self.Min_Stack[-1][1])
        self.Min_Stack.append((val, current_min))

    def pop(self) -> None:
        self.Min_Stack.pop()

    def top(self) -> int:
        return self.Min_Stack[-1][0]

    def getMin(self) -> int:
        return self.Min_Stack[-1][1]
