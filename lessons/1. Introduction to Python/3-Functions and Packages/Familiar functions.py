# Familiar functions
# Out of the box, Python offers a bunch of built-in functions to make your life as a data scientist easier. You already know two such functions: print() and type(). There are also functions like str(), int(), bool() and float() to switch between data types. You can find out about them here. These are built-in functions as well.

# Calling a function is easy. To get the type of 3.0 and store the output as a new variable, result, you can use the following:

# result = type(3.0)
# Instructions
# 100 XP
# Use print() in combination with type() to print out the type of var1.
# Use len() to get the length of the list var1. Wrap it in a print() call to directly print it out.
# Use int() to convert var2 to an integer. Store the output as out2.

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)


# Help!
# Maybe you already know the name of a Python function, but you still have to figure out how to use it. Ironically, you have to ask for information about a function with another function: help(). In IPython specifically, you can also use ? before the function name.

# To get help on the max() function, for example, you can use one of these calls:

# help(max)
# ?max
# Use the IPython Shell to open up the documentation on pow(). Do this by typing ?pow or help(pow) and hitting Enter.

# Which of the following statements is true?

# Instructions
# 50 XP
# Possible answers


# pow() takes three arguments: base, exp, and mod. Without mod, the function will return an error.

# pow() takes three required arguments: base, exp, and None.

#  -> true ans: pow() requires base and exp arguments; mod is optional.

# pow() takes two arguments: exp and mod. Missing exp results in an error.


# Multiple arguments
# In the previous exercise, you identified optional arguments by viewing the documentation with help(). You'll now apply this to change the behavior of the sorted() function.

# Have a look at the documentation of sorted() by typing help(sorted) in the IPython Shell.

# You'll see that sorted() takes three arguments: iterable, key, and reverse. In this exercise, you'll only have to specify iterable and reverse, not key.

# Two lists have been created for you.

# Can you paste them together and sort them in descending order?

# Instructions
# 100 XP
# Use + to merge the contents of first and second into a new list: full.
# Call sorted() and on full and specify the reverse argument to be True. Save the sorted list as full_sorted.
# Finish off by printing out full_sorted.

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)

# String Methods
# Strings come with a bunch of methods. Follow the instructions closely to discover some of them. If you want to discover them in more detail, you can always type help(str) in the IPython Shell.

# A string place has already been created for you to experiment with.

# Instructions
# 100 XP
# Use the .upper() method on place and store the result in place_up. Use the syntax for calling methods that you learned in the previous video.
# Print out place and place_up. Did both change?
# Print out the number of o's on the variable place by calling .count() on place and passing the letter 'o' as an input to the method. We're talking about the variable place, not the word "place"!

# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))


# List Methods
# Strings are not the only Python types that have methods associated with them. Lists, floats, integers and booleans are also types that come packaged with a bunch of useful methods. In this exercise, you'll be experimenting with:

# .index(), to get the index of the first element of a list that matches its input and
# .count(), to get the number of times an element appears in a list.
# You'll be working on the list with the area of different parts of a house: areas.

# Instructions
# 100 XP
# Use the .index() method to get the index of the element in areas that is equal to 20.0. Print out this index.
# Call .count() on areas to find out how many times 9.50 appears in the list. Again, simply print out this number.


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

# List Methods (2)
# Most list methods will change the list they're called on. Examples are:

# .append(), that adds an element to the list it is called on,
# .remove(), that removes the first element of a list that matches the input, and
# .reverse(), that reverses the order of the elements in the list it is called on.
# You'll be working on the list with the area of different parts of the house: areas.

# Instructions
# 100 XP
# Use .append() twice to add the size of the poolhouse and the garage again: 24.5 and 15.45, respectively. Make sure to add them in this order.
# Print out areas
# Use the .reverse() method to reverse the order of the elements in areas.
# Print out areas once more.

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)


# Import package
# Let's say you wanted to calculate the circumference and area of a circle. Here's what those formulas look like:

# C = 2Pir 
# A = Pir^2
# Rather than typing the number for pi, you can use the math package that contains the number

# For reference, ** is the symbol for exponentiation. For example 3**4 is 3 to the power of 4 and will give 81.

# Instructions
# 100 XP
# Import the math package.
# Use math.pi to calculate the circumference of the circle and store it in C.
# Use math.pi to calculate the area of the circle and store it in A.

# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))


# Selective import
# General imports, like import math, make all functionality from the math package available to you. However, if you decide to only use a specific part of a package, you can always make your import more selective:

# from math import pi
# Try the same thing again, but this time only use pi.

# Instructions
# 100 XP
# Perform a selective import from the math package where you only import the pi function.
# Use math.pi to calculate the circumference of the circle and store it in C.
# Use math.pi to calculate the area of the circle and store it in A.

# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))

# Different ways of importing
# There are several ways to import packages and modules into Python. Depending on the import call, you'll have to use different Python code.

# Suppose you want to use the function inv(), which is in the linalg subpackage of the scipy package. You want to be able to use this function as follows:

# my_inv([[1,2], [3,4]])
# Which import statement will you need in order to run the above code without an error?

# Instructions
# 50 XP
# Possible answers


# import scipy

# import scipy.linalg

# from scipy.linalg import my_inv

# -> True ans: from scipy.linalg import inv as my_inv