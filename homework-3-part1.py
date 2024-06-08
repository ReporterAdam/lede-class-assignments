# Adam Friedman
# 6-7-2024
# Homework 3, Part 1

#1 Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
my_list = [22, 90, 0, -10, 3, 22, 48]
#2 Display the number of elements in the list.
print(len(my_list))
#3 Display the 4th element of this list.
print(my_list[3])
#4 Display the sum of the 2nd and 4th element of the list.
print(int(my_list[1]) + int(my_list[3]))
#5 Display the 2nd-largest value in the list.
sorted_my_list = (sorted(my_list))
print(sorted_my_list[5])
#6 Display the last element of the original unsorted list
print(my_list[-1])
#7 Display the sum of all of the numbers divided by two.
sum_my_list = sum(my_list)
print(sum_my_list/2)
#8 Print whether the median or the mean of the numbers is higher
#There has to be a python code for statistics but I don't know it?!?!?
my_list_mean = sum_my_list/len(my_list)
my_list_median = ((sorted_my_list[2] + sorted_my_list[3])/2)
if my_list_mean > my_list_median:
    print("The mean is larger than the median.")
elif my_list_median > my_list_mean:
    print("The median is larger than the mean.")

#Dictionaries

#1) Sometimes dictionaries are used to describe multiple aspects of a single object. 
#Like, say, a movie. Define a dictionary called movie that works with the following code.

movie = {
    'title': 'Back to the Future',
    'year': '1985',
    'director': 'Robert Zemeckis'
}

print("My favorite movie is", movie['title'], "which was released in", movie['year'], 
"and was directed by", movie['director'])

#2) On the lines after that, add keys to the movie dictionary 
#for budget and revenue (you'll use code like movie['budget'] = 1000), 
#and print out the difference between the two.

movie['budget'] = 19000000
movie['revenue'] = 388800000

movie_profit_loss = (movie['revenue']) - (movie['budget'])

if movie_profit_loss > 0:
    print(movie['title'],"made $", "{:,}".format(movie_profit_loss))
elif movie_profit_loss < 0:
    print(movie['title'],"lost $", "{:,}".format(movie_profit_loss))
    

#3) If the movie cost more to make than it made in theaters, 
#print "That was a bad investment". 
#If the film's revenue was more than five times the amount it cost to make, print
#"That was a great investment." Otherwise print "That was an okay investment."
if movie['revenue'] * 5 > movie['budget']:
    print(movie['title'],"was a great investmemnt.")
elif movie_profit_loss < 0:
    print(movie['title'],"was a bad investment.")
else:
    print(movie['title'],"was an okay investment.")
    

#4) Sometimes dictionaries are used to describe the same aspects of many different objects. 
#Make ONE dictionary that describes the population of the boroughs of NYC. 
#Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m, 
#Queens has 2.3m and Staten Island has 470,000. 
#(Tip: keeping it all in either millions or thousands is a good idea)

nyc_borough_pop = {
    'Manhattan' : 1600000,
    'Brooklyn' : 2600000,
    'Bronx' : 1400000,
    'Queens': 2300000,
    'Staten Island' : 470000
}

#5) Display the population of Brooklyn.

print("The population of is Brooklyn is", "{:,}".format(nyc_borough_pop['Brooklyn']))

#6) Display the combined population of all five boroughs.

nyc_population = sum(nyc_borough_pop.values())

print("The population of all New York's boroughs is", "{:,}".format(nyc_population))

#7) Display what percent of NYC's population lives in Manhattan
percent_manhattan_in_nyc = round((nyc_borough_pop['Manhattan'] / nyc_population), 4) * 100
print(percent_manhattan_in_nyc, "percent of New York City's population lives in Manhattan")


