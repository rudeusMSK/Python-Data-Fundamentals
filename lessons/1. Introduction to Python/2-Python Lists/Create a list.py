# Create a list
# A list is a compound data type; you can group values together, like this:

# a = "is"
# b = "nice"
# my_list = ["my", "list", a, b]
# After measuring the height of your family, 
# you decide to collect some information on the house you're living in. 
# The areas of the different parts of your house are stored in separate variables in the exercise.

# Create a list, areas, that contains the area of the hallway (hall), kitchen (kit), living room (liv), bedroom (bed) and bathroom (bath), in this order. Use the predefined variables.
# Print areas with the print() function.

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)

# Create lists with different types

# Although it's not really common, a list can also contain a mix of Python types including strings, floats, and booleans.

# You're now going to add the room names to your list, so you can easily see both the room name and size together.

# Some of the code has been provided for you to get you started. Pay attention here! "bathroom" is a string, while bath is a variable that represents the float 9.50 you specified earlier.

# Instructions
# 100 XP
# Finish the code that creates the areas list. Build the list so that the list first contains the name of each room as a string and then its area. In other words, add the strings "hallway", "kitchen" and "bedroom" at the appropriate locations.
# Print areas again; is the printout more informative this time?

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)

# List of lists
# As a data scientist, you'll often be dealing with a lot of data, and it will make sense to group some of this data.

# Instead of creating a list containing strings and floats, representing the names and areas of the rooms in your house, you can create a list of lists.

# Remember: "hallway" is a string, while hall is a variable that represents the float 11.25 you specified earlier.

# Instructions
# 100 XP
# Finish the list of lists so that it also contains the bedroom and bathroom data. Make sure you enter these in order!
# Print out house; does this way of structuring your data make more sense?

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Subset and conquer
# Subsetting Python lists is a piece of cake. Take the code sample below, which creates a list x and then selects "b" from it. Remember that this is the second element, so it has index 1. You can also use negative indexing.

# x = ["a", "b", "c", "d"]
# x[1]
# x[-3] # same result!
# Remember the areas list from before, containing both strings and floats? Its definition is already in the script. Can you add the correct code to do some Python subsetting?

# Instructions
# 100 XP
# Print out the second element from the areas list (it has the value 11.25).
# Subset and print out the last element of areas, being 9.50. Using a negative index makes sense here!
# Select the number representing the area of the living room (20.0) and print it out.

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])

# Slicing and dicing
# Selecting single values from a list is just one part of the story. It's also possible to slice your list, which means selecting multiple elements from your list. Use the following syntax:

# my_list[start:end]
# The start index will be included, while the end index is not. However, it's also possible not to specify these indexes. If you don't specify the start index, Python figures out that you want to start your slice at the beginning of your list.

# Instructions
# 100 XP
# Use slicing to create a list, downstairs, that contains the first 6 elements of areas.
# Create upstairs, as the last 4 elements of areas. This time, simplify the slicing by omitting the end index.
# Print both downstairs and upstairs using print().

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

# Subsetting lists of lists
# A Python list can also contain other lists.

# To subset lists of lists, you can use the same technique as before: square brackets. This would look something like this for a list, house:

# house[2][0]
# Instructions
# 100 XP
# Subset the house list to get the float 9.5.

house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house[-1][1]

# Replace list elements
# To replace list elements, you subset the list and assign new values to the subset. You can select single elements or you can change entire list slices at once.

# For this and the following exercises, you'll continue working on the areas list that contains the names and areas of different rooms in a house.

# Instructions
# 100 XP
# Update the area of the bathroom to be 10.50 square meters instead of 9.50 using negative indexing.
# Make the areas list more trendy! Change "living room" to "chill zone". Don't use negative indexing this time.\

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"

# Extend a list
# If you can change elements in a list, you sure want to be able to add elements to it, right? You can use the + operator:

# x = ["a", "b", "c", "d"]
# y = x + ["e", "f"]
# You just won the lottery, awesome! You decide to build a poolhouse and a garage. Can you add the information to the areas list?

# Instructions
# 100 XP
# Use the + operator to paste the list ["poolhouse", 24.5] to the end of the areas list. Store the resulting list as areas_1.
# Further extend areas_1 by adding data on your garage. Add the string "garage" and float 15.45. Name the resulting list areas_2.

# Create the areas list (updated version)
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

# Delete list elements
# Finally, you can also remove elements from your list. You can do this with the del statement:

# x = ["a", "b", "c", "d"]
# del x[1]
# Pay attention here: as soon as you remove an element from a list, the indexes of the elements that come after the deleted element all change!

# Unfortunately, the amount you won with the lottery is not that big after all and it looks like the poolhouse isn't going to happen. You'll need to remove it from the list. You decide to remove the corresponding string and float from the areas list.

# Instructions
# 100 XP
# Delete the string and float for the "poolhouse" from your areas list.
# Print the updated areas list.

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[10]
del areas[10]

# Print the updated list
print(areas)

# Inner workings of lists
# Some code has been provided for you in this exercise: a list with the name areas and a copy named areas_copy.

# Currently, the first element in the areas_copy list is changed and the areas list is printed out. If you hit the run code button you'll see that, although you've changed areas_copy, the change also takes effect in the areas list. That's because areas and areas_copy point to the same list.

# If you want to prevent changes in areas_copy from also taking effect in areas, you'll have to do a more explicit copy of the areas list with list() or by using [:].

# Instructions
# 100 XP
# Change the second command, that creates the variable areas_copy, such that areas_copy is an explicit copy of areas. After your edit, changes made to areas_copy shouldn't affect areas. Submit the answer to check this.

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)