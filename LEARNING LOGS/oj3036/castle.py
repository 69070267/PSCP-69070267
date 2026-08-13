"""IDK"""
import math

N = int(input())

if N == 1:
    print(0)
else:
    R = math.ceil(math.sqrt(N))
    walls = 2 * (R - 1)
    if (N + R) % 2 != 0:
        walls -= 1
    print(walls)
