from enum import Enum


class Type(Enum):
    SQUARE = 1
    CROSS = 2
    DIAMOND = 3


class Node:

    def __init__(self, x, y, i):
        self.x = x
        self.y = y
        self.i = i


class NeighboringNodes:

    def __init__(self, size, debug):
        self.size = size
        self.debug = debug
        self.grid()

    def grid(self):
        self.grid = [[0 for x in range(self.size)] for x in range(self.size)]
        # iterate over each element in grid and assign a new node
        count = 1
        for r in range(self.size):
            for c in range(self.size):
                self.grid[r][c] = Node(c, r, count)
                count += 1

        # print x,y,i of each node if debug is True
        if self.debug:
            for r in range(self.size):
                for c in range(self.size):
                    node = self.grid[r][c]
                    print((node.x, node.y, node.i))

    def get_coords(self, i):
        if i <= 0 or i > self.size ** 2:
            raise Exception("index out of bounds!")
        # if element in last column
        if i % self.size == 0:
            x = self.size - 1
            y = (i // self.size) - 1
        else:
            x = (i % self.size) - 1
            y = i // self.size

        return x, y

    def get_neighbors(self, m, type, x, y=None):
        # if index is given instead of x,y coords, get coords
        if y == None:
            try:
                x, y = self.get_coords(x)
            except:
                raise Exception("index out of bounds!")

        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            raise Exception("coordinates out of bounds!")

        if m <= 0 or m > self.size // 2:
            raise Exception("radius m must be > than 0 and <= size/2!")

        if type is Type.SQUARE:
            nbrs = []
            # iterate over row and col of elements within radius of node
            for i in range(y - m, y + m + 1):
                for j in range(x - m, x + m + 1):
                    if i >= 0 and i < self.size and j >= 0 and j < self.size:
                        if not (i == y and j == x):
                            coords = (j, i)
                            nbrs.append(coords)
            return nbrs

        if type is Type.CROSS:
            nbrs = []
            # iterate over elements in vertical line
            for i in range(y - m, y + m + 1):
                if i >= 0 and i < self.size and i != y:
                    coords = (x, i)
                    nbrs.append(coords)
            # iterate over elements in horizontal line
            for j in range(x - m, x + m + 1):
                if j >= 0 and j < self.size and j != x:
                    coords = (j, y)
                    nbrs.append(coords)

            return nbrs

        if type is Type.DIAMOND:
            nbrs = []
            # iterate over top triangle of diamond
            count = 1
            for line in range(y - m, y + 1):
                if line >= 0 and line < self.size:
                    offset = x - (count // 2)
                    for i in range(offset, offset + count):
                        if i >= 0 and i < self.size:
                            if not (i == x and line == y):
                                coords = (i, line)
                                nbrs.append(coords)
                count += 2
            # iterate over bottom triangle of diamond
            count = 1
            for line in range(y + m, y, -1):
                if line >= 0 and line < self.size:
                    offset = x - (count // 2)
                    for i in range(offset, offset + count):
                        if i >= 0 and i < self.size:
                            if not (i == x and line == y):
                                coords = (i, line)
                                nbrs.append(coords)
                count += 2

            return nbrs

