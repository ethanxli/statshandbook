class StringChain:

    def __init__(self, words):
        self.words = words
        self.longestChainMap = dict()
        self.longestChain = 0

        for w in words:
            self.longestChainMap[w] = 1

    def getLongestChainHelper(self, s):
        for c in range(len(s)):
            p = str(s[:c] + s[c+1:])
            if p in self.longestChainMap and (self.longestChainMap[p]+1 > self.longestChainMap[s]):
                self.longestChainMap[s] = self.longestChainMap[p]+1

        if self.longestChainMap[s] > self.longestChain:
            self.longestChain = self.longestChainMap[s]

    def getLongestChain(self):
        self.words.sort(key=len)
        for w in self.words:
            self.getLongestChainHelper(w)

        return self.longestChain



s = StringChain(["bdca","a", "b", "ba", "bca", "bda"])

print s.getLongestChain()
