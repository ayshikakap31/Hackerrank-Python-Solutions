#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    ele = list(s.split(' '))
    new_ele = []
    for i in range(len(ele)):
        name_part = ele[i]
        if name_part.isalpha():
            if len(name_part)>1:
                updated_name_part = name_part[0].upper() + name_part[1:]
            else:
                updated_name_part = name_part[0].upper()
            new_ele.append(updated_name_part)
        else:
            updated_name_part = name_part
            new_ele.append(updated_name_part)
    new_s = ' '.join(new_ele)
            
    return new_s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
