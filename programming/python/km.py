'''
Strategy:
1. Calculate a list of possible moves based on input grid and movetype.
2. Calculate sum of possible moves. Strategy is to build up a memoized sum of
possible combinations starting from a list of valid digits.

At the start, validDigits is the number of possible combinations with 1 number
starting from validDigits[i]. (i.e., validDigits[2] is the number of possible
combinations of length 1).

We iterate from 1 to pathlength n. At each step, we loop through the possible
moves from all current valid positions, and add the past possible combinations
to the current value of validDigits.

The final number of combinations is the sum of validDigits at step n.
'''

import numpy as np

def isNum(x):
    return isinstance(x, (int))

def stringIsInt(s):
    try:
        return int(s)
    except ValueError:
        return s

class NumberMoves:

    def __init__(self, movetype, pathlength, starting, grid):
        if movetype != 'knight' and movetype != 'bishop':
            raise

        self.movetype = movetype

        self.grid = grid
        self.gridRows = len(self.grid)
        self.gridCols = len(self.grid[0])
        self.validMoves = dict()

        self.pathlength = pathlength
        self.validDigits = [0,0,1,1,1,1,1,1,1,1]

        self.validDigits = [0] * 10

        for i in starting:
            self.validDigits[i] = 1
        # self.validMatrix =

        self.possibleMovesMatrix = np.matrix((self.pathlength,10))
        self.calcValidMoves()

    def calcValidMovesKnight(self,position):
        x,y = position
        self.validMoves[(x,y)] = []

        for (x1,y1) in [(-2,1),(-2,-1),(2,-1),(2,1),(1,-2),(1,2),(-1,-2),(-1,2)]:
            xn = x + x1
            yn = y + y1
            if (xn >= 0 and xn < self.gridRows and yn >= 0 and yn < self.gridCols and isNum(self.grid[xn][yn])):
                self.validMoves[(x,y)].append((xn,yn))

    def calcValidMovesBishop(self,position):
        x,y = position
        self.validMoves[(x,y)] = []

        for (x1,y1) in [(-1,1),(-1,-1),(1,1),(1,-1)]:
            xn,yn = x,y
            while(xn >= 0 and xn < self.gridRows and yn >= 0 and yn < self.gridCols):
                xn+=x1
                yn+=y1
                if (xn >= 0 and xn < self.gridRows and yn >= 0 and yn < self.gridCols and isNum(self.grid[xn][yn])):
                    self.validMoves[(x,y)].append((xn,yn))

    def calcValidMoves(self):

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if(isNum(self.grid[i][j])):
                    if(self.movetype=='knight'):
                        self.calcValidMovesKnight((i,j))
                    else:
                        self.calcValidMovesBishop((i,j))

    def knumbers(self):
        curRow = self.validDigits
        for row in range(1, self.pathlength):
            last = curRow
            curRow = [0 for i in range(10)]
            for cur in self.validMoves:
                x,y = cur
                for (xn,yn) in self.validMoves[cur]:
                    curRow[self.grid[xn][yn]] += last[self.grid[x][y]] #memoize

        return sum(curRow)

try:
    movetype = raw_input()
    numlength = int(raw_input())
    startingdigits = [int(j) for j in raw_input().split(' ')]

    rows = raw_input()
    cols = raw_input()
    grid = []

    for i in range(int(rows)):
        grid.append([stringIsInt(j) for j in raw_input().split(' ')])

    n = NumberMoves(movetype,numlength,startingdigits,grid)
    print n.knumbers()

except: #some parsing error
    print 0
