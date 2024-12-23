# Random float
# Randomness has many uses in science, art, statistics, cryptography, gaming, gambling, and other fields. You're going to use randomness to simulate a game.

# All the functionality you need is contained in the random package, a sub-package of numpy. In this exercise, you'll be using two functions from this package:

# seed(): sets the random seed, so that your results are reproducible between simulations. As an argument, it takes an integer of your choosing. If you call the function, no output will be generated.
# rand(): if you don't specify any arguments, it generates a random float between zero and one.
# Instructions
# 100 XP
# Import numpy as np.
# Use seed() to set the seed; as an argument, pass 123.
# Generate your first random float with rand() and print it out.

# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())

# Roll the dice
# In the previous exercise, you used rand(), that generates a random float between 0 and 1.

# As Hugo explained in the video you can just as well use randint(), also a function of the random package, to generate integers randomly. The following call generates the integer 4, 5, 6 or 7 randomly. 8 is not included.

# import numpy as np
# np.random.randint(4, 8)
# NumPy has already been imported as np and a seed has been set. Can you roll some dice?

# Instructions
# 100 XP
# Use randint() with the appropriate arguments to randomly generate the integer 1, 2, 3, 4, 5 or 6. This simulates a dice. Print it out.
# Repeat the outcome to see if the second throw is different. Again, print out the result.

# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))

# Determine your next move
# In the Empire State Building bet, your next move depends on the number you get after throwing the dice. We can perfectly code this with an if-elif-else construct!

# The sample code assumes that you're currently at step 50. Can you fill in the missing pieces to finish the script? numpy is already imported as np and the seed has been set to 123, so you don't have to worry about that anymore.

# Instructions
# 100 XP
# Roll the dice. Use randint() to create the variable dice.
# Finish the if-elif-else construct by replacing ___:
# If dice is 1 or 2, you go one step down.
# if dice is 3, 4 or 5, you go one step up.
# Else, you throw the dice again. The number on the dice is the number of steps you go up.
# Print out dice and step. Given the value of dice, was step updated correctly?

# Numpy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1

elif dice > 2 and dice < 6 :
    step = step + 1
    
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice,step)


# The next step
# Before, you have already written Python code that determines the next step based on the previous step. Now it's time to put this code inside a for loop so that we can simulate a random walk.

# numpy has been imported as np.

# Instructions
# 100 XP
# Make a list random_walk that contains the first step, which is the integer 0.
# Finish the for loop:
# The loop should run 100 times.
# On each iteration, set step equal to the last element in the random_walk list. You can use the index -1 for this.
# Next, let the if-elif-else construct update step for you.
# The code that appends step to random_walk is already coded.
# Print out random_walk.


# Numpy is imported, seed is set

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)


# How low can you go?
# Things are shaping up nicely! You already have code that calculates your location in the Empire State Building after 100 dice throws. However, there's something we haven't thought about - you can't go below 0!

# A typical way to solve problems like this is by using max(). If you pass max() two arguments, the biggest one gets returned. For example, to make sure that a variable x never goes below 10 when you decrease it, you can use:

# x = max(10, x - 1)
# Instructions
# 100 XP
# Use max() in a similar way to make sure that step doesn't go below zero if dice <= 2.
# Hit Submit Answer and check the contents of random_walk.


# Numpy is imported, seed is set

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)

# Visualize the walk
# Let's visualize this random walk! Remember how you could use matplotlib to build a line plot?

# import matplotlib.pyplot as plt
# plt.plot(x, y)
# plt.show()
# The first list you pass is mapped onto the x axis and the second list is mapped onto the y axis.

# If you pass only one argument, Python will know what to do and will use the index of the list to map onto the x axis, and the values in the list onto the y axis.

# Instructions
# 100 XP
# Add some lines of code after the for loop:

# Import matplotlib.pyplot as plt.
# Use plt.plot() to plot random_walk.
# Finish off with plt.show() to actually display the plot.

# Numpy is imported, seed is set

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()


# Simulate multiple walks
# A single random walk is one thing, but that doesn't tell you if you have a good chance at winning the bet.

# To get an idea about how big your chances are of reaching 60 steps, you can repeatedly simulate the random walk and collect the results. That's exactly what you'll do in this exercise.

# The sample code already sets you off in the right direction. Another for loop is wrapped around the code you already wrote. It's up to you to add some bits and pieces to make sure all of the results are recorded correctly.

# Note: Don't change anything about the initialization of all_walks that is given. Setting any number inside the list will cause the exercise to crash!

# Instructions
# 100 XP
# Instructions
# 100 XP
# Fill in the specification of the for loop so that the random walk is simulated five times.
# After the random_walk array is entirely populated, append the array to the all_walks list.
# Finally, after the top-level for loop, print out all_walks.

# Numpy is imported; seed is set

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range(5,10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)

# Visualize all walks
# all_walks is a list of lists: every sub-list represents a single random walk. If you convert this list of lists to a NumPy array, you can start making interesting plots! matplotlib.pyplot is already imported as plt.

# The nested for loop is already coded for you - don't worry about it. For now, focus on the code that comes after this for loop.

# Instructions
# 100 XP
# Use np.array() to convert all_walks to a NumPy array, np_aw.
# Try to use plt.plot() on np_aw. Also include plt.show(). Does it work out of the box?
# Transpose np_aw by calling np.transpose() on np_aw. Call the result np_aw_t. Now every row in np_all_walks represents the position after 1 throw for the five random walks.
# Use plt.plot() to plot np_aw_t; also include a plt.show(). Does it look better this time?


# Initialization
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

# Number of walks and steps
num_walks = 5
num_steps = 100

# Create a list to store all walks
all_walks = []

# Generate multiple random walks
for _ in range(num_walks):
    random_walk = [0]
    for x in range(num_steps):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to a NumPy array
np_aw = np.array(all_walks)

# Plotting the original walks
plt.plot(np_aw)
plt.title("Random Walks")
plt.xlabel("Steps")
plt.ylabel("Position")
plt.show()

# Transpose np_aw
np_aw_t = np.transpose(np_aw)

plt.clf()

# Plotting the transposed walks
plt.plot(np_aw_t)
plt.title("Transposed Random Walks")
plt.xlabel("Walks")
plt.ylabel("Position after each step")
plt.show()


# Implement clumsiness
# With this neatly written code of yours, changing the number of times the random walk should be simulated is super-easy. You simply update the range() function in the top-level for loop.

# There's still something we forgot! You're a bit clumsy and you have a 0.5% chance of falling down. That calls for another random number generation. Basically, you can generate a random float between 0 and 1. If this value is less than or equal to 0.005, you should reset step to 0.

# Instructions
# 100 XP
# Change the range() function so that the simulation is performed 20 times.
# Finish the if condition so that step is set to 0 if a random float is less or equal to 0.005. Use np.random.rand().


# numpy and matplotlib imported, seed set
import matplotlib.pyplot as plt
import numpy as np

# clear the plot so it doesn't get cluttered if you run this many times
plt.clf()

# Simulate random walk 20 times
all_walks = []
for i in range(20) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if(np.random.rand() <= 0.005) :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()


# Plot the distribution
# All these fancy visualizations have put us on a sidetrack. We still have to solve the million-dollar problem: What are the odds that you'll reach 60 steps high on the Empire State Building?

# Basically, you want to know about the end points of all the random walks you've simulated. These end points have a certain distribution that you can visualize with a histogram.

# Note that if your code is taking too long to run, you might be plotting a histogram of the wrong data!

# Instructions
# 100 XP
# To make sure we've got enough simulations, go crazy. Simulate the random walk 500 times.
# From np_aw_t, select the last row. This contains the endpoint of all 500 random walks you've simulated. Store this NumPy array as ends.
# Use plt.hist() to build a histogram of ends. Don't forget plt.show() to display the plot.


all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()


# Calculate the odds
# The histogram of the previous exercise was created from a NumPy array ends, that contains 500 integers. Each integer represents the end point of a random walk. To calculate the chance that this end point is greater than or equal to 60, you can count the number of integers in ends that are greater than or equal to 60 and divide that number by 500, the total number of simulations.

# Well then, what's the estimated chance that you'll reach at least 60 steps high if you play this Empire State Building game? The ends array is everything you need; it's available in your Python session so you can calculate it.

# Instructions
# 50 XP
# Possible answers


# 48.8%

# 76.6%

# -> true ans: 78.4%

# 95.9%