#!/bin/python3

import os

#
# Complete the 'cubeSum' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY operations
#

def cubeSum(n, operations):
    vals = {}  # key-value: (x, y, z) -> int
    results = []
    for operation in operations:
        cmmd, *args = operation.split()
        match cmmd:
            case 'UPDATE':
                x, y, z, w = [int(_) for _ in args]
                vals[(x, y, z)] = w
            case 'QUERY':
                x, y, z, a, b, c = [int(_) for _ in args]
                ttl = 0
                for k, v in vals.items():
                    if x <= k[0] <= a and y <= k[1] <= b and z <= k[2] <= c:
                        ttl += v
                results.append(ttl)
            case _:
                raise ValueError("Not a valid operation.")
    return results

# Setup Main

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    T = int(input().strip())
    for T_itr in range(T):
        first_multiple_input = input().rstrip().split()
        matSize = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        ops = []
        for _ in range(m):
            ops_item = input()
            ops.append(ops_item)
        res = cubeSum(matSize, ops)
        fptr.write('\n'.join(map(str, res)))
        fptr.write('\n')
    fptr.close()
