import time
import math

start_time = time.time()

def russian(a, b):
    x = a; y = b
    z = 0
    while x > 0:
        if x == 7 and z == 84:
            print(y)
        if x % 2 == 1: z = z + y
        y = y << 1
        x = x >> 1
    return z

# print(russian(63, 12))

# print("--- %s seconds ---" % (time.time() - start_time))


def naive(a,b):
    x = a; y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

# print(naive(20, 12))

def rec_naive(a, b):
    if a == 0:
        return 0
    return b + rec_naive(a-1, b)

# print( rec_naive(17,6))

# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
    # your code here
    tour = []
    l = len(graph)
    for i in range(l):
        t = edge(graph[i], graph[(i + 1) % 1])
        tour.append(t)
    return tour


def edge(x, y):
    return (x, y) if x < y else (y, x)

print(find_eulerian_tour([(1, 2), (2, 3), (3, 1)]))
