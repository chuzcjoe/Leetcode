class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxsize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxsize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        else:
            return self.stack.pop(-1)

    def increment(self, k: int, val: int) -> None:
        for i in range(0, k):
            if i >= len(self.stack):
                break
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)