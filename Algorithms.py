import time
import math

# start_time = time.time()
#
# def russian(a, b):
#     x = a; y = b
#     z = 0
#     while x > 0:
#         if x == 7 and z == 84:
#             print(y)
#         if x % 2 == 1: z = z + y
#         y = y << 1
#         x = x >> 1
#     return z
#
# # print(russian(63, 12))
#
# # print("--- %s seconds ---" % (time.time() - start_time))
#
#
# def naive(a,b):
#     x = a; y = b
#     z = 0
#     while x > 0:
#         z = z + y
#         x = x - 1
#     return z
#
# # print(naive(20, 12))
#
# def rec_naive(a, b):
#     if a == 0:
#         return 0
#     return b + rec_naive(a-1, b)
#
# # print( rec_naive(17,6))
#
# # Find Eulerian Tour
# #
# # Write a function that takes in a graph
# # represented as a list of tuples
# # and return a list of nodes that
# # you would follow on an Eulerian Tour
# #
# # For example, if the input graph was
# # [(1, 2), (2, 3), (3, 1)]
# # A possible Eulerian tour would be [1, 2, 3, 1]
#
# def find_eulerian_tour(graph):
#     # your code here
#     tour = []
#     l = len(graph)
#     for i in range(l):
#         t = edge(graph[i], graph[(i + 1) % 1])
#         tour.append(t)
#     return tour
#
#
# def edge(x, y):
#     return (x, y) if x < y else (y, x)
#
# # print(find_eulerian_tour([(1, 2), (2, 3), (3, 1)]))
#
#
# # sqrt = 256**(1/2.0)
# # print(sqrt)
#
# x = 15 * 16
# print(2 * x)
#
# def make_link(G, node1, node2):
#     if node1 not in G:
#         G[node1] = {}
#     (G[node1])[node2] = 1
#     if node2 not in G:
#         G[node2] = {}
#     (G[node2])[node1] = 1
#     return G
#
# G = {}
#
# n = 256
# side = int(math.sqrt(n))
#
# # Add in the edges
# for i in range(side):
#     for j in range(side):
#         if i < side-1: make_link(G, (i, j), (i + 1, j))
#         if j < side - 1: make_link(G, (i, j), (i, j + 1))
#
# # How many nodes?
# print(len(G))
#
# # How many edges?
# print(sum([len(G[node]) for node in G.keys()])/2)
#
# print(2 * n * n)
# print(6 * n)
# print(20 * math.log(n, 2))
#
#
# print("\nHow many edges in a complete graph on n nodes?\n")
#
# def getNodeArray(n):
#     nodeArray = []
#     i = 0
#     while i < n:
#         i = i + 1
#         nodeArray.append(i)
#     return nodeArray
#
# def clique(n):
#
#     edges = 0
#     nodeArray = getNodeArray(n)
#     for node in nodeArray:
#         edges = edges + (node - 1)
#
#     return edges
#
# # print(clique(3))
# # print(clique(5))
# # print(clique(6))
#
# for n in range(1,10):
#     numNodes = n
#     numEdges = clique(n)
#     print("A graph with " + str(numNodes) + " nodes has " + str(numEdges) + " edges.")
#
# for n in range(1,10):
#     print([(n), clique(n), n * (n-1) / 2])
#
# n = 15
# print(math.log(n))
# print(n)
# print(math.pow(2,n))

# print("Write a program that returns the number of edges "
#       "in a star network that has `n` nodes ")
#
# def star_network(n):
#     # return number of edges
#
#     return n - 1
# i = 1
# for n in range (1,11):
#     print("run " + str(i))
#     i = i + 1
#     print(star_network(n))


# n = 11310
# print(4 * n * n)
# print(math.pow(math.log(n), 7))
# print(9 * n * (math.pow(math.log(n), 2)))
# print(math.pow(n, 2/3))
#
# print(n * n)

# Generate a combination lock graph given a list of nodes
#

# def make_link(G, node1, node2):
#     if node1 not in G:
#         G[node1] = {}
#     (G[node1])[node2] = 1
#     if node2 not in G:
#         G[node2] = {}
#     (G[node2])[node1] = 1
#     return G
#
# def create_combo_lock(nodes):
#     G = {}
#     make_link(G, nodes[0], nodes[1])
#     for i in range(2, len(nodes)):
#         # chain part
#         make_link(G, nodes[i-1], nodes[i])
#         # star part
#         make_link(G, 0, nodes[i])
#
#     # your code here
#     # for i in range(nodes - 1):
#     #     G[i] = [i,i+1]
#     #     G[0].append([0,i+1])
#     #     # G[0] = G[0].append([i+1])
#
#
#     return G
#
# print(create_combo_lock(range(5)))

# Erdos Renyi Graph where n = 256 and p = 0.25
# edges = 0
# n = 256
# p = 0.25
# edges = n * (n-1) * p / 2
#
# print(edges)

# CC(ORD)
# v = "ORD"
# Kv = 4
# Nv = 2
#
# CC = 2 * Nv / (Kv * (Kv - 1))
# print(CC)

##################################################################
# Traversal...
# Call this routine on nodes being visited for the first time
def mark_component(G, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbor in G[node]:
        if neighbor not in marked:
            total_marked += mark_component(G, neighbor, marked)
    return total_marked


def check_connection(G, v1, v2):
    # Return True if v1 is connected to v2 in G
    # or False if otherwise
    marked = {}
    mark_component(G, v1, marked)
    return v2 in marked


def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


def test():
    edges = [('a', 'g'), ('a', 'd'), ('g', 'c'), ('g', 'd'),
             ('b', 'f'), ('f', 'e'), ('e', 'h')]
    G = {}
    for v1, v2 in edges:
        make_link(G, v1, v2)

    print(check_connection(G, 'a', 'c'))
    print(check_connection(G, 'a', 'b'))


    # assert check_connection(G, "a", "c") == True
    # assert check_connection(G, 'a', 'b') == False

test()

