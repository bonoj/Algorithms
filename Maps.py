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

locations = {'North America': {'USA': ['Mountain View']}}

# """Print the following (using "print").
# 1. A list of all cities in the USA in
# alphabetic order.
# 2. All cities in Asia, in alphabetic
# order, next to the name of the country.
# In your output, label each answer with a number
# so it looks like this:
# 1
# American City
# American City
# 2
# Asian City - Country
# Asian City - Country"""
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}
# print(locations['North America']['USA'])

usa_sorted = sorted(locations['North America']['USA'])
for city in usa_sorted:
    print(city)


asia_cities = []
for countries, cities in locations['Asia'].items():
    city_country = cities[0] + " - " + countries
    asia_cities.append(city_country)

asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print(city)

