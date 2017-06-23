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

# print(find_eulerian_tour([(1, 2), (2, 3), (3, 1)]))


# sqrt = 256**(1/2.0)
# print(sqrt)

x = 15 * 16
print(2 * x)

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

G = {}

n = 256
side = int(math.sqrt(n))

# Add in the edges
for i in range(side):
    for j in range(side):
        if i < side-1: make_link(G, (i, j), (i + 1, j))
        if j < side - 1: make_link(G, (i, j), (i, j + 1))

# How many nodes?
print(len(G))

# How many edges?
print(sum([len(G[node]) for node in G.keys()])/2)

print(2 * n * n)
print(6 * n)
print(20 * math.log(n, 2))


print("\nHow many edges in a complete graph on n nodes?\n")

def getNodeArray(n):
    nodeArray = []
    i = 0
    while i < n:
        i = i + 1
        nodeArray.append(i)
    return nodeArray

def clique(n):

    edges = 0
    nodeArray = getNodeArray(n)
    for node in nodeArray:
        edges = edges + (node - 1)

    return edges

# print(clique(3))
# print(clique(5))
# print(clique(6))

for n in range(1,10):
    numNodes = n
    numEdges = clique(n)
    print("A graph with " + str(numNodes) + " nodes has " + str(numEdges) + " edges.")

for n in range(1,10):
    print([(n), clique(n), n * (n-1) / 2])

n = 15
print(math.log(n))
print(n)
print(math.pow(2,n))