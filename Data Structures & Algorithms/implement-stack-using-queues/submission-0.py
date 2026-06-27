class MyStack:

    def __init__(self):
        self.Q1=deque()

    def push(self, x: int) -> None:
        self.Q1.append(x)

        for _ in range(len(self.Q1) - 1): #_ is a throw away var, does nt mtr yaawr
            self.Q1.append(self.Q1.popleft())
        

    def pop(self) -> int:
        return self.Q1.popleft()

    def top(self) -> int:
        return self.Q1[0]
        

    def empty(self) -> bool:
        return len(self.Q1)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()