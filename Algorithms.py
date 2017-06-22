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

print(russian(20, 7))

print("--- %s seconds ---" % (time.time() - start_time))

# print("--- %s seconds ---" % "John")

# start_time = "john"

# print(start_time)