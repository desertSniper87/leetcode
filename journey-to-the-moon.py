#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce
#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

def journeyToMoon(n, astronaut):
    groups = [{i} for i in range(n)]
    for pair in astronaut:
        appended = False
        for group in groups:
            if any(x in group for x in pair):
                group.update(pair)
                appended = True
                break
        if not appended:
            groups.append(set(pair))
    print(groups)

    s = 1

    for g in groups:
        s *= len(g)

    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)
    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
