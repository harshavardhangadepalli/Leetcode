class MinStack:
    l = list()
    def __init__(self):
        self.l = list()
        return

    def push(self, val: int) -> None:
        self.l.append(val)
        return

    def pop(self) -> None:
        self.l.pop()
        return

    def top(self) -> int:
        return self.l[len(l)-1]

    def getMin(self) -> int:
        return min(self.l)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()