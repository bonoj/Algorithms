# Dictionaries!

# udacity = {}
# udacity['u'] = 1
# udacity['d'] = 2
# udacity['a'] = 3
# udacity['c'] = 4
# udacity['i'] = 5
# udacity['t'] = 6
# udacity['y'] = 7
#
# print(udacity)
# # {'u': 1, 'd': 2, 'a': 3, 'c': 4, 'i': 5, 't': 6, 'y': 7}
#
# print(udacity['t'])
#
# dictionary = {}
# dictionary['d'] = [1]
# dictionary['i'] = [2]
# dictionary['c'] = [3]
# dictionary['t'] = [4]
# dictionary['i'].append(5)
# dictionary['o'] = [6]
# dictionary['n'] = [7]
# dictionary['a'] = [8]
# dictionary['r'] = [9]
# dictionary['y'] = [10]
# print(dictionary)

"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

# locations = {'North America': {'USA': ['Mountain View']}}
#
# # """Print the following (using "print").
# # 1. A list of all cities in the USA in
# # alphabetic order.
# # 2. All cities in Asia, in alphabetic
# # order, next to the name of the country.
# # In your output, label each answer with a number
# # so it looks like this:
# # 1
# # American City
# # American City
# # 2
# # Asian City - Country
# # Asian City - Country"""
# locations['North America']['USA'].append('Atlanta')
# locations['Asia'] = {'India': ['Bangalore']}
# locations['Asia']['China'] = ['Shanghai']
# locations['Africa'] = {'Egypt': ['Cairo']}
# # print(locations['North America']['USA'])
#
# usa_sorted = sorted(locations['North America']['USA'])
# for city in usa_sorted:
#     print(city)
#
#
# asia_cities = []
# for countries, cities in locations['Asia'].items():
#     city_country = cities[0] + " - " + countries
#     asia_cities.append(city_country)
#
# asia_sorted = sorted(asia_cities)
# for city in asia_sorted:
#     print(city)

# Hash Tables and Hash Functions

# In this quiz, you'll write your own hash table and
# hash function that uses string keys. Your table will
# store strings in buckets by their first two letters,
# according to the formula below:
#
# Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter
# You can assume that the string will have at least two letters,
# and the first two characters are uppercase letters
# (ASCII values from 65 to 90). You can use the Python
# function ord() to get the ASCII value of a letter, and chr()
# to get the letter associated with an ASCII value.
#
# You'll create a HashTable class, methods to store and lookup values,
# and a helper function to calculate a hash value given a string.
# You cannot use a Python dictionary—only lists!
# And remember to store lists at each bucket, and not
# just the string itself.
# For example, you can store "UDACITY" at index 8568 as ["UDACITY"].

# """Write a HashTable class that stores strings
# in a hash table, where keys are calculated
# using the first two letters of the string."""


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def store(self, string):
        """Input a string that's stored in
        the table."""
        hashValue = self.calculate_hash_value(string)
        if hashValue != -1:
            if self.table[hashValue] != None:
                self.table[hashValue].append(string)
            else:
                self.table[hashValue] = [string]


    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hashValue = self.calculate_hash_value(string)
        if hashValue != -1:
            if self.table[hashValue] != None:
                if string in self.table[hashValue]:
                    return hashValue
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        value = ord(string[0]) * 100 + ord(string[1])
        return value


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))
print(hash_table.lookup('UDACITY'))