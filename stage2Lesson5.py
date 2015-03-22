beatles = [['John', '1940'],
		   ['Paul', '1942'],
		   ['George', '1943'],
		   ['Ringo', '1940']]

print beatles[3][0]		   

# Given the variable countries defined as:

#             Name    Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# Write code to print out the capital of India
# by accessing the list

print countries[1][1]


# What multiple of Romania's population is the population
# of China? Calculate this by accessing the list and
# dividing the population of China (1350)
# by the population of Romania (21).
# Please print your result.

china_pop = countries[0][2]
romania_pop = countries[2][2]

multiple = china_pop / romania_pop
print multiple

# Mutation

p = ['H','e','l','l','o']
print p

p[0] = 'Y'
print p

# We defined:

stooges = ['Moe','Larry','Curly']

# but in some Stooges films, Curly was
# replaced by Shemp.

# Write one line of code that changes
# the value of stooges to be:

['Moe','Larry','Shemp']

# but does not create a new List
# object.
stooges[2] = 'Shemp'

print stooges

spy = [0, 0, 7]
agent = spy
spy[2] = agent[2] + 1
#print agent, spy

spy = [0,0,7]

def replace_spy(spy):
 	spy[2] = spy[2] + 1 
	return spy
	

print replace_spy(spy)


#append

stooges = ['Moe','Larry','Curly']
stooges.append('Shemp')

print stooges

p = [1, 2]
q = [3, 4]

p.append(q)
print len(p)
print p



# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.

def sum_list(p):
	result = 0
	for number in p:
		result = result + number
	return result

print sum_list([1, 7, 4])
#>>> 12

#print sum_list([9, 4, 10])
#>>> 23

#print sum_list([44, 14, 76])
#>>> 134





# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.

def measure_udacity(p):
	udacious = 'U'
	result = 0
	for e in p:
		if e[0] == udacious:
			result = result + 1
	return result



#print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

#rint measure_udacity(['Umika','Umberto'])
#>>> 2






# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(p,t):
	i = 0
	for e in p:
		if e == t:
			return i
		i = i + 1
	return -1



#print find_element([1,2,3],3)
#>>> 2

#print find_element(['alpha','beta'],'gamma')
#>>> -1


# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.
def find_element(p,t):
	if t in p:
		return p.index(t)
	else:
		return -1






print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1






