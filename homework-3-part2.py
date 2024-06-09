# Adam Friedman
# 6-7-24
# Homework 3, Part 2

#1) Make a list called "countries" - it should contain seven different countries 
#and NOT be in alphabetical order

country_list = ['United States', 'Canada', 'Mexico', 'Spain', 'England', 'Germany']

#2) Using a for loop, print each element of the list

for country in country_list: 
    print(country)

#3) Sort the list permanently.

country_list = sorted(country_list)

#4) Display the first element of the list.
print("The first element in the sorted list is", country_list[0])

#5) Display the second-to-last element of the list.
print("The second last element in the sorted list is", country_list[-2])

#6) Delete one of the countries from the list using its name.

country_list.remove('Spain')

#7) Using a for loop, print each country's name in all caps.

for country in country_list:
    print(country.upper())


#1) Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 
#'location_name', 'latitude' and 'longitude'. Pick a tree from: https://en.wikipedia.org/wiki/List_of_trees

tree = {
    'name' : 'Irish strawberry tree',
    'species' : 'A. unedo',
    'year' : 260,
    'location_name' : 'Ireland',
    'latitude' : 54.607869,
    'longitude' : -5.926437

}

#2) Print the sentence "{name} is a {years} year old tree that is in {location_name}"

print("The", tree['name'], "is a" , tree['year'], "year old tree that is in", tree['location_name'])

#3) The coordinates of New York City are 40.7128° N, 74.0059° W. 
#Check to see if the tree is south of NYC, and print 
#"The tree {name} in {location} is south of NYC" if it is. 
#If it isn't, print "The tree {name} in {location} is north of NYC"

nyc = {
    'latitude' : 40.7128,
    'longitude' : -74.0059
}

if tree['latitude'] > nyc['latitude']:
    print("The", tree['name'], "is north of New York City")
else:
    print("New York City is north of the", tree['name'])


#4) Ask the user how old they are. If they are older than the tree, 
#display "you are {XXX} years older than {name}." 
#If they are younger than the tree, display "{name} was {XXX} years old when you were born."

user_age = input("How old are you? Answer with a number. ")
user_age = int(user_age)
user_older = user_age - tree['year']
user_younger = tree['year'] - user_age

if user_age > tree['year']:
    print("You are", user_older, "years older than the", tree['name'], "tree.")
elif user_age < tree['year']:
    print("You are", user_younger, "years younger than the", tree['name'], "tree.")


#PART TWO: Lists of dictionaries

#1) Make a list of dictionaries of five places across the world 
#- (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago. 
#Each dictionary should include each city's name and latitude/longitude (see note above).

#Note: Going to be honest I used chatgpt4 for this mainly, because pulling lat/long through it is
#SOOOOOOO much easier

cities = {
    "Moscow": {"latitude": 55.7558, "longitude": 37.6176},
    "Tehran": {"latitude": 35.6895, "longitude": 51.389},
    "Falkland_islands": {"latitude": -51.7963, "longitude": 59.5236},
    "Seoul": {"latitude": 37.5665, "longitude": 126.978},
    "Santiago": {"latitude": -33.4489, "longitude": 70.6693}
}


#2) Loop through the list, printing each city's name 
#and whether it is above or below the equator 
#(How do you know? Think hard about the latitude.). 
#When you get to the Falkland Islands, also display the message 
#"The Falkland Islands are a biogeographical part of the mild Antarctic zone," 
#which is a sentence I stole from Wikipedia.

for city, coordinates in cities.items(): 
    if coordinates['latitude'] > 0:
        print(city, "is above the equator")
    elif city == 'Falkland_islands':
        print("The Falkland Islands are a biogeographical part of the mild Antarctic zone")
    else:
        print(city, "is below the equator")
        
#3) Loop through the list, printing whether each city 
#is north of south of your tree from the previous section.

for city, coordinates in cities.items(): 
    if coordinates['latitude'] > tree['latitude']:
        print(city, "is above the tree the location of the", tree['name'])
    else:
        print(city, "is below the tree the location of the", tree['name'])