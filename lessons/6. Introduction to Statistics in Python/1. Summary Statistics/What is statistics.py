# Mean and median
# In this chapter, you'll be working with the food_consumption dataset from 2018 Food Carbon Footprint Index by nu3. The food_consumption dataset contains the number of kilograms of food consumed per person per year in each country and food category (consumption), and its carbon footprint (co2_emissions) measured in kilograms of carbon dioxide, or CO2.

# In this exercise, you'll compute measures of center to compare food consumption in the US and Belgium using your pandas and numpy skills.

# pandas is imported as pd for you and food_consumption is pre-loaded.

# Instructions
# 100 XP
# Import numpy with the alias np.
# Subset food_consumption to get the rows where the country is 'USA'.
# Calculate the mean of food consumption in the usa_consumption DataFrame, which is already created for you.
# Calculate the median of food consumption in the usa_consumption DataFrame.

# Import numpy with alias np
import numpy as np

# Subset country for USA: usa_consumption
usa_consumption = food_consumption[food_consumption['country'] == 'USA']

# Calculate mean consumption in USA
print(usa_consumption['consumption'].mean())

# Calculate median consumption in USA
print(usa_consumption['consumption'].median())


# Mean vs. median
# In the video, you learned that the mean is the sum of all the data points divided by the total number of data points, and the median is the middle value of the dataset where 50% of the data is less than the median, and 50% of the data is greater than the median. In this exercise, you'll compare these two measures of center.

# pandas is loaded as pd, numpy is loaded as np, and food_consumption is available.

# Instructions 1/4
# 30 XP
# Import matplotlib.pyplot with the alias plt.
# Subset food_consumption to get the rows where food_category is 'rice'.
# Create a histogram of co2_emission in rice_consumption DataFrame and show the plot.
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Histogram of co2_emission for rice and show plot
rice_consumption['co2_emission'].hist()
plt.show()

# Instructions 2/4
# 20 XP
# Question
# Take a look at the histogram you just created of different countries' CO2 emissions for rice. Which of the following terms best describes the shape of the data?

# Possible answers


# No skew

# Left-skewed

# -> true ans: Right-skewed

# Instructions 3/4
# 30 XP
# Use .agg() to calculate the mean and median of co2_emission for rice.

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Calculate mean and median of co2_emission with .agg()
print(rice_consumption['co2_emission'].agg([np.mean, np.median]))


# Instructions 4/4
# 20 XP
# Question
# Given the skew of this data, what measure of central tendency best summarizes the kilograms of CO2 emissions per person per year for rice?

# Possible answers


# Mean

# -> true ans: Median

# Both mean and median


# Variance and standard deviation
# Variance and standard deviation are two of the most common ways to measure the spread of a variable, and you'll practice calculating these in this exercise. Spread is important since it can help inform expectations. For example, if a salesperson sells a mean of 20 products a day, but has a standard deviation of 10 products, there will probably be days where they sell 40 products, but also days where they only sell one or two. Information like this is important, especially when making predictions.

# pandas has been imported as pd, numpy as np, and matplotlib.pyplot as plt; the food_consumption DataFrame is also available.

# Instructions
# 100 XP
# Calculate the variance and standard deviation of co2_emission for each food_category with the .groupby() and .agg() methods; compare the values of variance and standard deviation.
# Create a histogram of co2_emission for the beef in food_category and show the plot.
# Create a histogram of co2_emission for the eggs in food_category and show the plot.


# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var, np.std]))

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Create histogram of co2_emission for food_category 'beef'
food_consumption[food_consumption['food_category'] == 'beef']['co2_emission'].hist()
# Show plot
plt.show()

# Create histogram of co2_emission for food_category 'eggs'
food_consumption[food_consumption['food_category'] == 'eggs']['co2_emission'].hist()
# Show plot
plt.show()


# Quartiles, quantiles, and quintiles
# Quantiles are a great way of summarizing numerical data since they can be used to measure center and spread, as well as to get a sense of where a data point stands in relation to the rest of the data set. For example, you might want to give a discount to the 10% most active users on a website.

# In this exercise, you'll calculate quartiles, quintiles, and deciles, which split up a dataset into 4, 5, and 10 pieces, respectively.

# Both pandas as pd and numpy as np are loaded and food_consumption is available.

# Instructions 1/3
# 35 XP
# Calculate the quartiles of the co2_emission column of food_consumption.
# Calculate the quartiles of co2_emission
quartiles = np.quantile(food_consumption['co2_emission'], [0, 0.25, 0.5, 0.75, 1])
print(quartiles)

# Calculate the six quantiles that split up the data into 5 pieces (quintiles) of the co2_emission column of food_consumption.
# Calculate the quintiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], [0, 0.2, 0.4, 0.6, 0.8, 1]))

# Calculate the eleven quantiles of co2_emission that split up the data into ten pieces (deciles).
# Calculate the deciles of co2_emission
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 11)))


# Finding outliers using IQR
# Outliers can have big effects on statistics like mean, as well as statistics that rely on the mean, such as variance and standard deviation. Interquartile range, or IQR, is another way of measuring spread that's less influenced by outliers. IQR is also often used to find outliers. If a value is less than 
# Q1 - 1.5 x IQR
# #  or greater than 
# Q3 + 1.5 x IQR
# , it's considered an outlier. In fact, this is how the lengths of the whiskers in a matplotlib box plot are calculated.

# Diagram of a box plot showing median, quartiles, and outliers

# In this exercise, you'll calculate IQR and use it to find some outliers. pandas as pd and numpy as np are loaded and food_consumption is available.

# Instructions 1/4
# 25 XP
# Instructions 1/4
# 25 XP
# Calculate the total co2_emission per country by grouping by country and taking the sum of co2_emission. Store the resulting DataFrame as emissions_by_country.
# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

print(emissions_by_country)

# Instructions 2/4
# 25 XP
# Compute the first and third quartiles of emissions_by_country and store these as q1 and q3.
# Calculate the interquartile range of emissions_by_country and store it as iqr.
# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

# Compute the first and third quartiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1


# Instructions 3/4
# 25 XP
# Calculate the lower and upper cutoffs for outliers of emissions_by_country, and store these as lower and upper.


# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

# Compute the first and third quantiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr


# Instructions 4/4
# 25 XP
# Subset emissions_by_country to get countries with a total emission greater than the upper cutoff or a total emission less than the lower cutoff.

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

# Compute the first and third quantiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Subset emissions_by_country to find outliers
outliers = emissions_by_country[(emissions_by_country < lower) | (emissions_by_country > upper)]
print(outliers)