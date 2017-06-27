import time
import math
import random

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

# ##################################################################
# # Traversal...
# # Call this routine on nodes being visited for the first time
# def mark_component(G, node, marked):
#     marked[node] = True
#     total_marked = 1
#     for neighbor in G[node]:
#         if neighbor not in marked:
#             total_marked += mark_component(G, neighbor, marked)
#     return total_marked
#
#
# def check_connection(G, v1, v2):
#     # Return True if v1 is connected to v2 in G
#     # or False if otherwise
#     marked = {}
#     mark_component(G, v1, marked)
#     return v2 in marked
#
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
#
# def test():
#     edges = [('a', 'g'), ('a', 'd'), ('g', 'c'), ('g', 'd'),
#              ('b', 'f'), ('f', 'e'), ('e', 'h')]
#     G = {}
#     for v1, v2 in edges:
#         make_link(G, v1, v2)
#
#     print(check_connection(G, 'a', 'c'))
#     print(check_connection(G, 'a', 'b'))
#
#
#     # assert check_connection(G, "a", "c") == True
#     # assert check_connection(G, 'a', 'b') == False
#
# test()
#

# Rewrite `mark_component` to not use recursion
# and instead use the `open_list` data structure
# discussed in lecture
#

# def mark_component(G, node, marked):
#     marked[node] = True
#     total_marked = 1
#     for neighbor in G[node]:
#         if neighbor not in marked:
#             total_marked += mark_component(G, neighbor, marked)
#     return total_marked

# def mark_component(G, node, marked):
#     open_list = [node]
#     total_marked = 1
#     marked[node] = True
#
#     while len(open_list) > 0:
#         print(open_list)
#         print(marked)
#         node = open_list.pop()
#         for neighbor in G[node]:
#             if neighbor not in marked:
#                 open_list.append(neighbor)
#                 marked[neighbor] = True
#                 total_marked += 1
#     return total_marked
#
#
# #########
# # Code for testing
# #
# def make_link(G, node1, node2):
#     if node1 not in G:
#         G[node1] = {}
#     (G[node1])[node2] = 1
#     if node2 not in G:
#         G[node2] = {}
#     (G[node2])[node1] = 1
#     return G
#
#
# def test():
#     test_edges = [(1, 2), (2, 3), (3, 4), (4, 5), (6,7)]
#     G = {}
#     for n1, n2 in test_edges:
#         make_link(G, n1, n2)
#     marked = {}
#     assert mark_component(G, 1, marked) == 5
#     assert 1 in marked
#     assert 2 in marked
#     assert 3 in marked
#     assert 4 in marked
#     assert 5 in marked
#     assert 6 not in marked
#     print(marked)
#
#
# print(test())


# #
# # Write centrality_max to return the maximum distance
# # from a node to all the other nodes it can reach
# #
#
# def centrality_max(G, v):
#     # your code here
#     distance_from_start = {}
#     open_list = [v]
#     distance_from_start[v] = 0
#     max_distance = 0
#
#     while len(open_list) > 0:
#         current = open_list[0]
#         del open_list[0]
#         for neighbor in G[current].keys():
#             # print(neighbor)
#             if neighbor not in distance_from_start:
#                 distance_from_start[neighbor] = distance_from_start[current] + 1
#                 # print(distance_from_start[neighbor])
#                 if distance_from_start[neighbor] > max_distance:
#                     max_distance = distance_from_start[neighbor]
#                 open_list.append(neighbor)
#     # return (sum(distance_from_start.values()) + 0.0) / len(distance_from_start)
#
#     # print(max_distance)
#     print(max(distance_from_start.values()) == max_distance)
#     return max(distance_from_start.values())
#
# #################
# # Testing code
# #
# def make_link(G, node1, node2):
#     if node1 not in G:
#         G[node1] = {}
#     (G[node1])[node2] = 1
#     if node2 not in G:
#         G[node2] = {}
#     (G[node2])[node1] = 1
#     return G
#
# def test():
#     chain = ((1,2), (2,3), (3,4), (4,5), (5,6))
#     G = {}
#     for n1, n2 in chain:
#         make_link(G, n1, n2)
#     assert centrality_max(G, 1) == 5
#     assert centrality_max(G, 3) == 3
#     tree = ((1, 2), (1, 3),
#             (2, 4), (2, 5),
#             (3, 6), (3, 7),
#             (4, 8), (4, 9),
#             (6, 10), (6, 11))
#     G = {}
#     for n1, n2 in tree:
#         make_link(G, n1, n2)
#     assert centrality_max(G, 1) == 3
#     assert centrality_max(G, 11) == 6
#
# def myTest():
#     chain = ((1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6,7), (7,8))
#     G = {}
#     for n1, n2 in chain:
#         make_link(G, n1, n2)
#     centrality_max(G, n1)
#
# # print(myTest())
#
# print(test())

# Bridge Edges
#
# First some utility functions
#

# def make_link(G, node1, node2, r_or_g):
#     # modified make_link to apply
#     # a color to the edge instead of just 1
#     if node1 not in G:
#         G[node1] = {}
#     (G[node1])[node2] = r_or_g
#     if node2 not in G:
#         G[node2] = {}
#     (G[node2])[node1] = r_or_g
#     return G
#
# def get_children(S, root, parent):
#     """returns the children from following the
#     green edges"""
#     return [n for n, e in S[root].items()
#             if ((not n == parent) and
#                 (e == 'green'))]
#
# def get_children_all(S, root, parent):
#     """returns the children from following
#     green edges and the children from following
#     red edges"""
#     green = []
#     red = []
#     for n, e in S[root].items():
#         if n == parent:
#             continue
#         if e == 'green':
#             green.append(n)
#         if e == 'red':
#             red.append(n)
#     return green, red
#
# #################
#
# def create_rooted_spanning_tree(G, root):
#     # use DFS from the root to add edges and nodes
#     # to the tree.  The first time we see a node
#     # the edge is green, but after that its red
#     open_list = [root]
#     S = {root:{}}
#     while len(open_list) > 0:
#         node = open_list.pop()
#         neighbors = G[node]
#         for n in neighbors:
#             if n not in S:
#                 # we haven't seen this node, so
#                 # need to use a green edge to connect
#                 # it
#                 make_link(S, node, n, 'green')
#                 open_list.append(n)
#             else:
#                 # we have seen this node,
#                 # but, first make sure that
#                 # don't already have the edge
#                 # in S
#                 if node not in S[n]:
#                     make_link(S, node, n, 'red')
#     return S
#
# ##################
#
# def _post_order(S, root, parent, val, po):
#     children = get_children(S, root, parent)
#     for c in children:
#         val = _post_order(S, c, root, val, po)
#     po[root] = val
#     return val + 1
#
# def post_order(S, root):
#     po = {}
#     _post_order(S, root, None, 1, po)
#     return po
#
#
# ##################
#
# def _number_descendants(S, root, parent, nd):
#     # number of descendants is the
#     # sum of the number of descendants of a nodes
#     # children plus one
#     children = get_children(S, root, parent)
#     nd_val = 1
#     for c in children:
#         # recursively calculate the number of descendants
#         # for the children
#         nd_val += _number_descendants(S, c, root, nd)
#     nd[root] = nd_val
#     return nd_val
#
# def number_of_descendants(S, root):
#     nd = {}
#     _number_descendants(S, root, None, nd)
#     return nd
#
#
# #
# # Since highest and lowest post order will follow
# # a similar method, I only wrote one method
# # that can be used for both
# #
# def _general_post_order(S, root, parent, po, gpo, comp):
#     green, red = get_children_all(S, root, parent)
#     val = po[root]
#     for c in green:
#         # recursively find the low/high post order value of the children
#         test = _general_post_order(S, c, root, po, gpo, comp)
#         # and save the low/highest one
#         if comp(val, test):
#             val = test
#     for c in red:
#         test = po[c]
#         # and also look at the direct children
#         # from following red edges
#         # and save the low/highest one if needed
#         if comp(val, test):
#             val = test
#     gpo[root] = val
#     return val
#
# def lowest_post_order(S, root, po):
#     lpo = {}
#     _general_post_order(S, root, None, po, lpo, lambda x, y: x > y)
#     return lpo
#
# def highest_post_order(S, root, po):
#     hpo = {}
#     _general_post_order(S, root, None, po, hpo, lambda x, y: x < y)
#     return hpo
#
# #
# # Now put everything together
# #
#
# def bridge_edges(G, root):
#     S = create_rooted_spanning_tree(G, root)
#     po = post_order(S, root)
#     nd = number_of_descendants(S, root)
#     lpo = lowest_post_order(S, root, po)
#     hpo = highest_post_order(S, root, po)
#     bridges = []
#     open_list = [(root, None)]
#     # walk down the tree and see which edges are
#     # tree edges
#     while len(open_list) > 0:
#         node, parent = open_list.pop()
#         for child in get_children(S, node, parent):
#             # all of these edges are automatically green (get_children only
#             # follows green edges)
#             # so only need to check the other two conditions
#             if hpo[child] <= po[child] and lpo[child] > (po[child] - nd[child]):
#                 bridges.append((node, child))
#             open_list.append((child, node))
#     return bridges
#
# print()

# #            animal       speed   weight lifespan brain
# #                          (mph)   (kg)  (years) mass (g)
# animals = [("dog",          46,   35,     13,  280    ),
#            ("elephant",     30, 3500,     50, 6250    ),
#            ("frog",          5,    0.5,    8,    3    ),
#            ("hippopotamus", 45, 1600,     45,  573    ),
#            ("horse",        40,  385,     30, 642     ),
#            ("human",        27,   80,     78, 2000    ),
#            ("lion",         50,  250,     30,  454    ),
#            ("mouse",         8,    0.025,  2,    0.625),
#            ("rabbit",       25,    4,     12,   40    ),
#            ("shark",        26,  230,     20,   92    ),
#            ("sparrow",      16,    0.024,  7,    2    )]
#
# def importance_rank(items, weights):
#     names = [item[0] for item in items]  # get the list of animal names
#     scores = [sum([a*b for (a,b) in zip(item[1:], weights)]) for item in items]  # get the list of overall scores for each animal
#     results = zip(scores,names) # make a list of tuple
#     res2 = sorted(results) # sort the tuple based on the score
#     return res2
#
# speedW = 9
# weightW = 2
# lifespanW = 55
# brainMassW = 331
# answer = importance_rank(animals, (speedW,weightW,lifespanW,brainMassW))
#
# for i in range(len(answer)):
#     print(i, answer[i][1], "(", answer[i][0], ")")
#
# print("\n")
# print(answer[3][1])

# list1 = [43, 21, 49, 48, 50, 51, 77, 79, 75, 87, 93]
# list1 = sorted(list1)
# midpoint = (list1[0] + list1[len(list1) - 1]) / 2
# print(midpoint)
# median = list1[int(len(list1) / 2)]
# print(median)
#
# print((midpoint + median) / 2)

# # List of node centrality values from an example graph
# L = [2, 3, 2, 3, 2, 4, 20, 19, 33, 2, 4, 5, 5, 65, 7, 4, 3, 6]
#
# def calculateMean(L):
#     total = 0
#     for i in range(len(L)):
#         total += L[i]
#     return (0.0 + total)/len(L)
#
# print(calculateMean(L))
#
# mean = ((0.0 + sum(L)) / len(L))
#
# print("Mean: " + str(mean))
#
# def max(L):
#     currentMax = L[0]
#     for i in range(len(L)):
#         if L[i] > currentMax:
#             currentMax = L[i]
#     return currentMax
#
# max = max(L)
#
# print("Max: " + str(max))

# import urllib.request
#
# target_url = "https://www.udacity.com/file?file_key=agpzfnVkYWNpdHl1ckALEgZDb3Vyc2UiBWNzMjE1DAsSCUNvdXJzZVJldhgBDAsSBFVuaXQY-qsODAsSDEF0dGFjaGVkRmlsZRiskBIM"
#
# txt = urllib.request.urlopen(target_url).read()
#
# names = txt.splitlines()
# stringOfNameData = []
# mostPopular = 0
# secondMostPopular = 0
# mostPopularName = ""
# secondMostPopularName = ""
# for name in names:
#     nameString = name.decode('utf-8')
#     # stringOfNames.append(nameString)
#     nameData = nameString.split(',')
#     stringOfNameData.append(nameData)
#     # if (name == names[0]):
#     #     mostPopular = nameData[2]
#     if (nameData[1] != 'F'):
#         continue
#
#     popularity = int(nameData[2])
#
#     if (popularity > mostPopular):
#         secondMostPopular = mostPopular
#         mostPopular = popularity
#         secondMostPopularName = mostPopularName
#         mostPopularName = nameData[0]
#
# print(mostPopular)
# print(mostPopularName)
# print(secondMostPopular)
# print(secondMostPopularName)

#
# Write partition to return a new array with
# all values less then `v` to the left
# and all values greater then `v` to the right
#

# import random
#
# def rank(L, v):
#     pos = 0
#     for val in L:
#         if val < v:
#             pos += 1
#     return pos
#
# def partition(L, v):
#     uP = []
#     lP = []
#
#     for i in L:
#         if i < v:
#             lP.append(i)
#         elif i > v:
#             uP.append(i)
#     return(lP, [v], uP)
#
#     return P
#
# def top_k(L, k):
#     v = L[random.randrange(len(L))]
#     (left,middle,right) = partition(L, v)
#     if len(left) == k: return left
#     if len(left) + 1 == k: return left + middle
#     if len(left) > k: return top_k(left, k)
#     return left + middle + top_k(right, k - len(left) - 1)
#
# L = [77, 55, 42, 34, 89, 51, 49, 31, 61, 72, 93, 12, 22]
#
# # print(partition(L, 34))
# # print(top_k(L, 6))
#
#
# # del(L[0])
# # print(L)
# # lastItem = L.pop(len(L) - 1)
# # print(lastItem)
# # print([lastItem] + L)
# print(L)
# for i in range(len(L) - 1):
#     L[0] = L.pop()
#     print(L)

#
# Given a list L of n numbers, find the mode
# (the number that appears the most times).
# Your algorithm should run in Theta(n).
# If there are ties - just pick one value to return
#
# from operator import itemgetter
#

####
# Test
#
# import time
# from random import randint
#
# def test():
#     assert 5 == mode([1, 5, 2, 5, 3, 5])
#     iterations = (10, 20, 30, 100, 200, 300, 1000, 5000, 10000, 20000, 30000)
#     times = []
#     for i in iterations:
#         L = []
#         for j in range(i):
#             L.append(randint(1, 10))
#         start = time.clock()
#         for j in range(500):
#             mode(L)
#         end = time.clock()
#         print(start, end)
#         times.append(float(end - start))
#     slopes = []
#     for (x1, x2), (y1, y2) in zip(zip(iterations[:-1], iterations[1:]), zip(times[:-1], times[1:])):
#         print (x1, x2), (y1, y2)
#         slopes.append((y2 - y1) / (x2 - x1))
#     # if mode runs in linear time,
#     # these factors should be close (kind of)
#     print(slopes)

#test()
#
# def mode(L):
#     counts = dict()
#     maxKey = None
#     maxValue = -1
#
#     for i in L:
#         if i not in counts:
#             counts[i] = 1
#         else:
#             counts[i] += 1
#         if counts[i] > maxValue:
#             maxKey = i
#             maxValue = counts[i]
#     return maxKey
#
#
# L = [11, 11, 11, 11, 11, 11, 11, 11, 22, 22,
#      22, 22, 22, 22, 22, 22, 34, 55, 12, 656, 23, 23526, 23, 234, 99, 96, 32, 324, 231]
#
# print(mode(L))

# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.stuff = []
#
#     def birthday(self):
#         self.age += 1
#
#     def addItems(self, item):
#         self.stuff += [item]
#
#
# s = Person("john", 33)
#
# print(s.name)
# print(s.age)
#
# s.birthday()
# print(s.age)
#
# s.addItems("algorithms")
# s.addItems("data structures")
# print(s.stuff)


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def getLastElem(self):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            return current

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        i = 1
        if position < 1:
            return None
        if self.head:
            while current.next and i < position:
                current = current.next
                i += 1
            if i == position:
                return current
            else:
                return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        i = 1
        if position > 1:
            while current and i < position:
                if i == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                i += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def insert_first(self, new_element):
        # current = self.head
        # while current:
        # current.next = current
        # current = new_element
        new_element.next = self.head
        self.head = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def delete_first(self):
        "Delete the first (head) element in the LinkedList and return it"
        current = self.head
        oldHead = self.head
        while current.next:
            current = current.next
        return oldHead

# # print(linkedList.head.value)
# #
# # print(linkedList.getLastElem().value)
# # print(linkedList.get_position(4).value)
# #
# # linkedList.delete(5)
# # print(linkedList.get_position(5).next)
# # print(linkedList.get_position(5).value)
#
# headElem = Element(1)
# linkedList = LinkedList(headElem)
#
# linkedList.append(Element(3))
# linkedList.append(Element(4))
# linkedList.append(Element(5))
# linkedList.insert(Element(2), 2)
#
# i = 1
# while i <= 5:
#     print(linkedList.get_position(i).value)
#     i += 1

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)
e6 = Element(6)
e7 = Element(7)

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()

stack = Stack(e1)
# print(stack.ll.head.value)
stack.push(e2)
# print(stack.ll.head.value)
stack.push(e3)
# print(stack.ll.head.value)
stack.push(e4)
stack.push(e5)
stack.push(e6)
stack.push(e7)


i = 1
while i <= 7:
    print(stack.ll.get_position(i).value)
    i += 1

poppedElem = stack.pop()
print(poppedElem.value)

