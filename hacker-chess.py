import math
import os
import random
import re
import sys



#

# Complete the 'verticalRooks' function below.

#

# The function is expected to return a STRING.

# The function accepts following parameters:

#  1. INTEGER_ARRAY r1

#  2. INTEGER_ARRAY r2

#

def make_checks():
    pass

def verticalRooks(n, r1, r2):
    # If you think it for a moment, the winner is decided just by the dimensions of the board AND how many rooks are stuck together when it starts the game
    # The best option is to always stick to the rook
    positions = []
    pass
    rooks_together = 0
    for i in range(n):
        positions.append(r1[i], r2[i])
    for position in positions:
        if abs(position[0] - position[1]) == 1:
            rooks_together += 1
        





if __name__ == '__main__':

    with open("hacker-chess-results", 'w') as fptr:

        t = int(input().strip())
        print(t)



        for t_itr in range(t):

            n = int(input().strip())

            r1 = []



            for _ in range(n):

                r1_item = int(input().strip())

                r1.append(r1_item)



            r2 = []



            for _ in range(n):

                r2_item = int(input().strip())

                r2.append(r2_item)



            result = verticalRooks(n, r1, r2)


            # fptr.write(result + '\n')