class BrowserHistory:

    def __init__(self, homepage: str):
        
        self.hist = []
        self.idx = 0
        self.hist.append(homepage)
        

    def visit(self, url: str) -> None:
        self.hist = self.hist[:self.idx+1]
        self.hist.append(url)
        self.idx += 1
        

    def back(self, steps: int) -> str:
        if steps > self.idx:
            self.idx = 0
            return self.hist[self.idx]
        else:
            self.idx = self.idx - steps
            return self.hist[self.idx]
        
        

    def forward(self, steps: int) -> str:
        if steps > len(self.hist) - self.idx - 1:
            self.idx = len(self.hist) - 1
            return self.hist[self.idx]
        else:
            self.idx = self.idx + steps
            return self.hist[self.idx]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)