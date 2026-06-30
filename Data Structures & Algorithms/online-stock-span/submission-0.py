class StockSpanner:

    def __init__(self):
        self.stack = []          # (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            #"Is the price at the top of the stack less than or equal to today's price?"
            span += self.stack.pop()[1]

        self.stack.append((price, span))

        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)