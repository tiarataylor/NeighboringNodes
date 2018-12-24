# NeighboringNodes
- Python program that creates a grid of nodes and finds the neighbors of specified node.
- MySQL database that contains denormalized node data.
## initializing NeighboringNodes
### NeighboringNodes(size, debug)
Creates NeighboringNodes instance, and calls grid function. 

Parameters:
- size: int >= 0
- debug: boolean

## Methods
### grid()
Creates grid of sizexsize nodes and prints grid nodes if debug is True.

### get_coords(i)
Returns tuple of x,y coords of node at index i. x and y are defined by list index (e.g. the top left node of a grid would have (0,0) coordinates). 

Parameters:
- i: int >= 1

### get_neighbors(m,type,x,y)
Returns list of x,y coords of the neighbors of the specified node based on neighborhood type.

Parameters:
- m: radius - int, 0 < m >= size/2
- type: neighborhood type - enum that must be either Type.DIAMOND, Type.SQUARE, or Type.CROSS
- x or i: x coord of specified node or index of specified node if x,y coords aren't given - int
- y(optional): y coord of specified node if given - int 

## SQL Database
Using mysql and sequelpro.
### Procedures:

- Run CREATE TABLE statement.
- import dummy_data.csv into table.

### Sample Queries:

- SELECT * FROM NeighboringNodes;
- SELECT * FROM NeighboringNodes where size = 3;
- #querying neighbor nodes and specified node with index 5 on grid of size 3  
SELECT * FROM NeighboringNodes where size = 3 and ((x = 1 and y <= 2 and y >=0) or (x >= 0 and x <= 2 and y = 1));
