class FreqStack:

    def __init__(self):
        self.freq={} #curr freq of the given value, js counts 
        self.group={} #shelves, shelf 1 = freq 1, shelf 2=freq 2 so on
        #as values freq inc they move up the shelf , from 1-2-3
        self.maxFreq=0
        
    def push(self, val: int) -> None:
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1
        #or self.freq[val] = self.freq.get(val, 0) + 1
        f=self.freq[val]

        if f > self.maxFreq:
            self.maxFreq = f
        
        if f not in self.group:
            self.group[f] = []

        self.group[f].append(val)

    def pop(self) -> int:
        val = self.group[self.maxFreq].pop()
        self.freq[val] -= 1

        if not self.group[self.maxFreq]:
            self.maxFreq -= 1

        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()