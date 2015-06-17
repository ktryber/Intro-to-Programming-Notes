# Investigating adding and appending to lists

# If you run the following four lines of codes, what are list1 and list2?

list1 = [1,2,3,4]
list2 = [1,2,3,4]

list1 = list1 + [5]
list2.append(5)

# to check, you can print them out using the print statements below.

#print "showing list1 and list2:"
#print list1
#print list2
#print "list 1 creates a new list where as list 2 is mutating the original list."

# What is the difference between these two pieces of code?

def proc(mylist):
    mylist = mylist + [6]

def proc2(mylist):
    mylist.append(6)

# Can you explain the results given by the four print statements below? Remove
# the hashes # and run the code to check.

#print "demonstrating proc"
#print list1
#proc(list1)
#print list1
#print
#print "demonstrating proc2"
#print list2
#proc2(list2)
#print list2

# Python has a special assignment syntax: +=.  Here is an example:

list3 = [1,2,3,4]


# Does this behave like list1 = list1 + [5] or list2.append(5)? Write a
# procedure, proc3 similar to proc and proc2, but for +=. When you've done
# that check your conclusion using the print-procedure call-print code as
# above.
def proc3(mylist):
	mylist += [5]

print proc3(list3)
print list3	

# What happens when you try:

list1 = list1 + [7,8,9]
list2.append([7,8,9])
list3 += [7,8,9]

# When you've understood the difference between the three methods,
# write a procedure list_test which takes three lists as inputs. You should
# mutate the first input list to include 'a' as the last entry, mutate the
# second to include the entries 'a', 'b', 'c' and finally the last list should
# not be mutated but a copy should be returned with the additional entry 'w'.


first_input = [1,2,3]
second_input = [4,5,6]
third_input = [7,8,9]


def list_test(x, y, z):
	x.append('a')
	y += ['a', 'b', 'c']
	z = z + ['w']
	return z


print list_test(first_input, second_input, third_input)
#>>> [7,8,9,'w']
print first_input
#>>> [1,2,3,'a']
print second_input
#>>> [4,5,6,'a','b','c']
print third_input
#>>> [7,8,9]



# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(list_of_numbers):
	product = 1
	for numbers in list_of_numbers:
		product *= numbers
	return product


print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

#print product_list([])
#>>> 1

# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(p):
	big = 0
	for i in p:
		if i > big:
			big = I




print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0



# Now you will write code for a function called 
# make_HTML_for_many_concepts. This function will take a list 
# of concepts (each of which is itself a list) and will return
# the appropriate string of HTML. 
#
# NOTE: You may want to call the make_HTML(concept) function
# which you defined in the previous exercise.
#
# This is the "generate_concept_HTML" function 
# from the previous work_session. You do not need to modify it.
def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

# This is one way you may have written make_HTML.
# You do not need to modify it.
def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

# This is an example of what a list of concepts might look like.
EXAMPLE_LIST_OF_CONCEPTS = [ ['Python', 'Python is a Programming Language'],
                             ['For Loop', 'For Loops allow you to iterate over lists'],
                             ['Lists', 'Lists are sequences of data'] ]

# This is the function you will write.
def make_HTML_for_many_concepts(list_of_concepts):
	HTML = ""
	for concept in list_of_concepts:
		concept_HTML = make_HTML(concept)
		HTML = HTML + concept_HTML
	return HTML
	

print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)
# The previous line of code should print the following
"""
<div class="concept">
    <div class="concept-title">
        Python
    </div>
    <div class="concept-description">
        Python is a Programming Language
    </div>
</div>
<div class="concept">
    <div class="concept-title">
        For Loop
    </div>
    <div class="concept-description">
        For Loops allow you to iterate over lists
    </div>
</div>
<div class="concept">
    <div class="concept-title">
        Lists
    </div>
    <div class="concept-description">
        Lists are sequences of data
    </div>
</div>
"""
