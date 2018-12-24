#mysql
CREATE TABLE NeighboringNodes (size INT,i INT, x INT, y INT, INDEX(size), PRIMARY KEY(size,i));
SELECT * FROM NeighboringNodes;
SELECT * FROM NeighboringNodes where size = 3;
#querying neighbor nodes and specified node with index 5 on grid of size 3
SELECT * FROM NeighboringNodes where size = 3 and ((x = 1 and y <= 2 and y >=0) or (x >= 0 and x <= 2 and y = 1));
