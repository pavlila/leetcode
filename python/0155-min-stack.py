# one stack - getMin O(n)
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        return None

    def pop(self) -> None:
        self.stack.pop(-1)
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        mini = 0

        for i, val in enumerate(self.stack):
            if i == 0:
                mini = val
            elif val < mini:
                mini = val
                
        return mini
    
# two stacks - getMin O(1)
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        return None

    def pop(self) -> None:
        val = self.stack.pop(-1)
        if self.min_stack[-1] == val:
            self.min_stack.pop()
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]