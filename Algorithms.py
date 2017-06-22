import time
import math

start_time = time.time()

def russian(a, b):
    x = a; y = b
    z = 0
    while x > 0:
        if x % 2 == 1: z = z + y
        y = y << 1
        x = x >> 1
    return z

# print(russian(20, 7))

# print("--- %s seconds ---" % (time.time() - start_time))

# print("--- %s seconds ---" % "John")

# start_time = "john"

# print(start_time)


def naive(a,b):
    x = a; y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

print(naive(20, 12))

def rec_naive(a, b):
    if a == 0:
        return 0
    return b + rec_naive(a-1, b)

print( rec_naive(17,6))
