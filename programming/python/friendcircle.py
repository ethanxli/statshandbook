from collections import deque

class FriendCircle:

    def __init__(self, fmap):
        self.visited = set()
        self.fmap = fmap
        self.count = 0

    '''
    Use a BFS to find the number of connected components (friend circles)
    '''

    def bfs(self, node, fmap):

        q = deque()
        q.append(node)
        self.visited.add(node)

        while q:
            node = q.popleft()
            for nextf, isfriend in enumerate(fmap[node]):
                if isfriend and nextf not in self.visited:
                    q.append(nextf)
                    self.visited.add(nextf)

    def run(self):
        for node in range(num):
            if node not in self.visited:
                self.bfs(node, fmap)
                self.count += 1

        print self.count


num = int(input())
#build a graph
fmap = [[ (1 if c=='Y' else 0) for c in str(raw_input())] for i in range(num)]

f = FriendCircle(fmap)
f.run()
