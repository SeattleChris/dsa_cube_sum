# dsa_cube_sum

Define a 3-D Matrix in which each block contains 0 initially. The first block is defined by the coordinates (1,1,1) and the last block is defined by the coordinates (n,n,n). There are two types of queries.

* UPDATE x y z W
  Update the value of block (x,y,z) to W.
* QUERY x1 y1 z1 x2 y2 z2
  Calculate the sum of the values of blocks whose x coordinate is between x1 and x2 (inclusive), y coordinate between y1 and y2 (inclusive) and z coordinate between z1 and z2 (inclusive).

## Function Description

cubeSum has the following parameters:

- *int n: the dimensions of the 3-d matrix
- string operations[m]: the operations to perform

Returns:
int[]: the results of each QUERY operation
