class MinStack:

    def __init__(self):
        self.arr = []
        self.min_arr = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.min_arr.append(min(self.min_arr[-1] if self.min_arr else float("inf"), val))
        

    def pop(self) -> None:
        self.arr.pop()
        self.min_arr.pop()

    def top(self) -> int:
        if len(self.arr) >= 1:
            return self.arr[-1]
        else:
            return None

    def getMin(self) -> int:
        return self.min_arr[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()