# Calculating probabilities
# You're in charge of the sales team, and it's time for performance reviews, starting with Amir. As part of the review, you want to randomly select a few of the deals that he's worked on over the past year so that you can look at them more deeply. Before you start selecting deals, you'll first figure out what the chances are of selecting certain deals.

# Recall that the probability of an event can be calculated by
 # P(event) = (# ways envent can happen) / (total # of possible outcomes)

# Both pandas as pd and numpy as np are loaded and amir_deals is available.

# Instructions 1/3
# 35 XP
# Count the number of deals Amir worked on for each product type using .value_counts() and store in counts.
# Count the deals for each product
counts = amir_deals['product'].value_counts()
print(counts)


# Instructions 2/3
# 35 XP
# Calculate the probability of selecting a deal for the different product types by dividing the counts by the total number of deals Amir worked on. Save this as probs.
# Count the deals for each product
counts = amir_deals['product'].value_counts()

# Calculate probability of picking a deal with each product
probs = counts / amir_deals.shape[0]
print(probs)

# Instructions 3/3
# 30 XP
# Question
# If you randomly select one of Amir's deals, what's the probability that the deal will involve Product C?

# Possible answers


# 15%

# 80.43%

# -> true ans: 8.43%

# 22.5%

# 124.3%


# Sampling deals
# In the previous exercise, you counted the deals Amir worked on. Now it's time to randomly pick five deals so that you can reach out to each customer and ask if they were satisfied with the service they received. You'll try doing this both with and without replacement.

# Additionally, you want to make sure this is done randomly and that it can be reproduced in case you get asked how you chose the deals, so you'll need to set the random seed before sampling from the deals.

# Both pandas as pd and numpy as np are loaded and amir_deals is available.

# Instructions 1/3
# 35 XP
# Set the random seed to 24.
# Take a sample of 5 deals without replacement and store them as sample_without_replacement.

# Set random seed
np.random.seed(24)

# Sample 5 deals without replacement
sample_without_replacement = amir_deals.sample(5)
print(sample_without_replacement)

# Take a sample of 5 deals with replacement and save as sample_with_replacement.
# Set random seed
np.random.seed(24)

# Sample 5 deals with replacement
sample_with_replacement = amir_deals.sample(5, replace=True)
print(sample_with_replacement)

# Instructions 3/3
# 30 XP
# Question
# What type of sampling is better to use for this situation?

# Possible answers

# With replacement

# -> true ans: Without replacement

# It doesn't matter



# A new restaurant opened a few months ago, and the restaurant's management wants to optimize its seating space based on the size of the groups that come most often. On one night, there are 10 groups of people waiting to be seated at the restaurant, but instead of being called in the order they arrived, they will be called randomly. In this exercise, you'll investigate the probability of groups of different sizes getting picked first. Data on each of the ten groups is contained in the restaurant_groups DataFrame.

# Remember that expected value can be calculated by multiplying each possible outcome with its corresponding probability and taking the sum. The restaurant_groups data is available. pandas is loaded as pd, numpy is loaded as np, and matplotlib.pyplot is loaded as plt.

# Instructions 1/4
# 25 XP
# Instructions 1/4
# 25 XP

# Create a histogram of the group_size column of restaurant_groups, setting bins to [2, 3, 4, 5, 6]. Remember to show the plot.
restaurant_groups['group_size'].hist(bins=np.linspace(2,6,5))
plt.show()


# Count the number of each group_size in restaurant_groups, then divide by the number of rows in restaurant_groups to calculate the probability of randomly selecting a group of each size. Save as size_dist.
# Reset the index of size_dist.
# Rename the columns of size_dist to group_size and prob.
# Create a histogram of restaurant_groups and show plot


# Create probability distribution
size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]

# Reset index and rename columns
size_dist = size_dist.reset_index()
size_dist.columns = ['group_size', 'prob']
print(size_dist)




# Calculate the expected value of the size_dist, which represents the expected group size, by multiplying the group_size by the prob and taking the sum.
# Create probability distribution
size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]
# Reset index and rename columns
size_dist = size_dist.reset_index()
size_dist.columns = ['group_size', 'prob']
# Calculate expected value
expected_value = np.sum(size_dist['group_size'] * size_dist['prob'])
print(expected_value)



# Calculate the probability of randomly picking a group of 4 or more people by subsetting for groups of size 4 or more and summing the probabilities of selecting those groups.
# Create probability distribution
size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]
# Reset index and rename columns
size_dist = size_dist.reset_index()
size_dist.columns = ['group_size', 'prob']

# Expected value
expected_value = np.sum(size_dist['group_size'] * size_dist['prob'])

# Subset groups of size 4 or more
groups_4_or_more = size_dist[size_dist['group_size'] >= 4]

# Sum the probabilities of groups_4_or_more
prob_4_or_more =  np.sum(groups_4_or_more['prob'])
print(prob_4_or_more)


# Data back-ups
# The sales software used at your company is set to automatically back itself up, but no one knows exactly what time the back-ups happen. It is known, however, that back-ups happen exactly every 30 minutes. Amir comes back from sales meetings at random times to update the data on the client he just met with. He wants to know how long he'll have to wait for his newly-entered data to get backed up. Use your new knowledge of continuous uniform distributions to model this situation and answer Amir's questions.

# Instructions 1/4
# 25 XP
# Instructions 1/4
# 25 XP


# To model how long Amir will wait for a back-up using a continuous uniform distribution, save his lowest possible wait time as min_time and his longest possible wait time as max_time. Remember that back-ups happen every 30 minutes.
# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30


# Import uniform from scipy.stats and calculate the probability that Amir has to wait less than 5 minutes, and store in a variable called prob_less_than_5.
# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Import uniform from scipy.stats
from scipy.stats import uniform

# Calculate probability of waiting less than 5 mins
prob_less_than_5 = uniform.cdf(5, min_time, max_time)
print(prob_less_than_5)


# Calculate the probability that Amir has to wait more than 5 minutes, and store in a variable called prob_greater_than_5.
# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Import uniform from scipy.stats
from scipy.stats import uniform

# Calculate probability of waiting more than 5 mins
prob_greater_than_5 = 1 - uniform.cdf(5, min_time, max_time)
print(prob_greater_than_5)


# Calculate the probability that Amir has to wait between 10 and 20 minutes, and store in a variable called prob_between_10_and_20.
# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Import uniform from scipy.stats
from scipy.stats import uniform

# Calculate probability of waiting 10-20 mins
prob_between_10_and_20 = uniform.cdf(20, min_time, max_time) - uniform.cdf(10, min_time, max_time)
print(prob_between_10_and_20)



# Simulating wait times
# To give Amir a better idea of how long he'll have to wait, you'll simulate Amir waiting 1000 times and create a histogram to show him what he should expect. Recall from the last exercise that his minimum wait time is 0 minutes and his maximum wait time is 30 minutes.

# As usual, pandas as pd, numpy as np, and matplotlib.pyplot as plt are loaded.

# Instructions 1/4
# 25 XP
# Set the random seed to 334.
# Set random seed to 334
np.random.seed(334)

#Instructions 2/4
# Import uniform from scipy.stats.
# Set random seed to 334
np.random.seed(334)

# Import uniform
from scipy.stats import uniform

#Instructions 3/4
# Generate 1000 wait times from the continuous uniform distribution that models Amir's wait time. Save this as wait_times.
# Set random seed to 334
np.random.seed(334)
# Import uniform
from scipy.stats import uniform
# Generate 1000 wait times between 0 and 30 mins
wait_times = uniform.rvs(0, 30, size=1000)
print(wait_times)



# Instructions 4/4
# 25 XP
# Create a histogram of the simulated wait times and show the plot.
# Set random seed to 334
np.random.seed(334)
# Import uniform
from scipy.stats import uniform
# Generate 1000 wait times between 0 and 30 mins
wait_times = uniform.rvs(0, 30, size=1000)
# Create a histogram of simulated times and show plot
plt.hist(wait_times)
plt.show()


# Simulating sales deals
# Assume that Amir usually works on 3 deals per week, and overall, he wins 30% of deals he works on. Each deal has a binary outcome: it's either lost, or won, so you can model his sales deals with a binomial distribution. In this exercise, you'll help Amir simulate a year's worth of his deals so he can better understand his performance.

# numpy is imported as np.

# Instructions 3/4
# 25 XP

# Import binom from scipy.stats and set the random seed to 10.
# Import binom from scipy.stats
from scipy.stats import binom
# Set random seed to 10
np.random.seed(10)



# Simulate 1 deal worked on by Amir, who wins 30% of the deals he works on.
# Import binom from scipy.stats
from scipy.stats import binom
# Set random seed to 10
np.random.seed(10)
# Simulate a single deal
print(binom.rvs(1, 0.3, size=1))



# Simulate a typical week of Amir's deals, or one week of 3 deals.
# Import binom from scipy.stats
from scipy.stats import binom
# Set random seed to 10
np.random.seed(10)
# Simulate 1 week of 3 deals
print(binom.rvs(3, 0.3, size=1))





# Simulate a year's worth of Amir's deals, or 52 weeks of 3 deals each, and store in deals.
# Print the mean number of deals he won per week.
# Import binom from scipy.stats
from scipy.stats import binom
# Set random seed to 10
np.random.seed(10)
# Simulate 52 weeks of 3 deals
deals = binom.rvs(3, 0.3, size=52)
# Print mean deals won per week
print(np.mean(deals))


# Calculating binomial probabilities
# Just as in the last exercise, assume that Amir wins 30% of deals. He wants to get an idea of how likely he is to close a certain number of deals each week. In this exercise, you'll calculate what the chances are of him closing different numbers of deals using the binomial distribution.

# binom is imported from scipy.stats.

# Instructions 1/3
# 35 XP
# What's the probability that Amir closes all 3 deals in a week? Save this as prob_3.
# Probability of closing 3 out of 3 deals
prob_3 = binom.pmf(3, 3, 0.3)
print(prob_3)

# Instructions 2/3
# 35 XP
# What's the probability that Amir closes 1 or fewer deals in a week? Save this as prob_less_than_or_equal_1.
# Probability of closing <= 1 deal out of 3 deals
prob_less_than_or_equal_1 = binom.cdf(1, 3, 0.3)
print(prob_less_than_or_equal_1)

# Instructions 3/3
# 30 XP
# What's the probability that Amir closes more than 1 deal? Save this as prob_greater_than_1.
# Probability of closing > 1 deal out of 3 deals
prob_greater_than_1 = 1 - binom.cdf(1, 3, 0.3)

print(prob_greater_than_1)


# How many sales will be won?
# Now Amir wants to know how many deals he can expect to close each week if his win rate changes. Luckily, you can use your binomial distribution knowledge to help him calculate the expected value in different situations. Recall from the video that the expected value of a binomial distribution can be calculated by 
# .

# Instructions
# 100 XP
# Calculate the expected number of sales out of the 3 he works on that Amir will win each week if he maintains his 30% win rate.
# Calculate the expected number of sales out of the 3 he works on that he'll win if his win rate drops to 25%.
# Calculate the expected number of sales out of the 3 he works on that he'll win if his win rate rises to 35%.

# Expected number won with 30% win rate
won_30pct = 3 * 0.3
print(won_30pct)

# Expected number won with 25% win rate
won_25pct = 3 * 0.25
print(won_25pct)

# Expected number won with 35% win rate
won_35pct = 3 * 0.35
print(won_35pct)