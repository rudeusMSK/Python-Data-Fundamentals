# Dealing with missing data
# It is important to deal with missing data before starting your analysis.

# One approach is to drop missing values if they account for a small proportion, typically five percent, of your data.

# Working with a dataset on plane ticket prices, stored as a pandas DataFrame called planes, you'll need to count the number of missing values across all columns, calculate five percent of all values, use this threshold to remove observations, and check how many missing values remain in the dataset.


# Instructions 1/3
# 35 XP
# Print the number of missing values in each column of the DataFrame.
# Count the number of missing values in each column
print(planes.isnull().sum())




# Instructions 2/3
# 35 XP
# Calculate how many observations five percent of the planes DataFrame is equal to.
# Count the number of missing values in each column
print(planes.isna().sum())

# Find the five percent threshold
threshold = len(planes) * 0.05



# Instructions 3/3
# 30 XP
# Create cols_to_drop by applying boolean indexing to columns of the DataFrame with missing values less than or equal to the threshold.
# Use this filter to remove missing values and save the updated DataFrame.
# Count the number of missing values in each column
print(planes.isna().sum())

# Find the five percent threshold
threshold = len(planes) * 0.05

# Create a filter
cols_to_drop = planes.columns[planes.isnull().sum() <= threshold]

# Drop missing values for columns below the threshold
planes.dropna(subset=cols_to_drop,  inplace=True)

print(planes.isna().sum())



# Strategies for remaining missing data
# The five percent rule has worked nicely for your planes dataset, eliminating missing values from nine out of 11 columns!

# Now, you need to decide what to do with the "Additional_Info" and "Price" columns, which are missing 300 and 368 values respectively.

# You'll first take a look at what "Additional_Info" contains, then visualize the price of plane tickets by different airlines.

# The following imports have been made for you:

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# Instructions 1/3
# 35 XP
# Print the values and frequencies of "Additional_Info".
# Check the values of the Additional_Info column
print(planes["Additional_Info"].value_counts())


# Instructions 2/3
# 35 XP
# Create a boxplot of "Price" versus "Airline".

# Check the values of the Additional_Info column
print(planes["Additional_Info"].value_counts())

# Create a box plot of Price by Airlin
sns.boxplot(data=planes, x='Airline', y='Price')

plt.show()

# Instructions 3/3
# 30 XP
# Question
# How should you deal with the missing values in "Additional_Info" and "Price"?
# Possible answers


# Remove the "Additional_Info" column and impute the mean for missing values of "Price".

# Remove "No info" values from "Additional_Info" and impute the median for missing values of "Price".

# Remove the "Additional_Info" column and impute the mean by "Airline" for missing values of "Price".

# -> true ans: Remove the "Additional_Info" column and impute the median by "Airline" for missing values of "Price".





# Imputing missing plane prices
# Now there's just one column with missing values left!

# You've removed the "Additional_Info" column from planes—the last step is to impute the missing data in the "Price" column of the dataset.

# As a reminder, you generated this boxplot, which suggested that imputing the median price based on the "Airline" is a solid approach!

# Box plot of plane ticket prices by Airline

# Instructions 1/3
# 35 XP
# Group planes by airline and calculate the median price.
# Calculate median plane ticket prices by Airline
airline_prices = planes.groupby('Airline')['Price'].median()

print(airline_prices)



# Instructions 2/3
# 35 XP
# Convert the grouped median prices to a dictionar
# Calculate median plane ticket prices by Airline
airline_prices = planes.groupby("Airline")["Price"].median()

print(airline_prices)

# Convert to a dictionary
prices_dict = airline_prices.to_dict()



# Instructions 3/3
# 30 XP
# Conditionally impute missing values for "Price" by mapping values in the "Airline" column based on prices_dict.
# Check for remaining missing values.
# Calculate median plane ticket prices by Airline
airline_prices = planes.groupby("Airline")["Price"].median()

print(airline_prices)

# Convert to a dictionary
prices_dict = airline_prices.to_dict()

# Map the dictionary to missing values of Price by Airline
planes['Price'] =planes['Price'].fillna(planes['Airline'].map(prices_dict))
# Check for missing values
print(planes.isnull().sum())



# Finding the number of unique values
# You would like to practice some of the categorical data manipulation and analysis skills that you've just seen. To help identify which data could be reformatted to extract value, you are going to find out which non-numeric columns in the planes dataset have a large number of unique values.

# pandas has been imported for you as pd, and the dataset has been stored as planes.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Filter planes for columns that are of "object" data type.
# Loop through the columns in the dataset.
# Add the column iterator to the print statement, then call the function to return the number of unique values in the column.
# Filter the DataFrame for object columns
non_numeric = planes.select_dtypes("object")

# Loop through columns
for i in non_numeric.columns:
  
  # Print the number of unique values
  print(f"Number of unique values in {i} column: ", non_numeric[i].nunique())


# Flight duration categories
# As you saw, there are 362 unique values in the "Duration" column of planes. Calling planes["Duration"].head(), we see the following values:

# 0        19h
# 1     5h 25m
# 2     4h 45m
# 3     2h 25m
# 4    15h 30m
# Name: Duration, dtype: object
# Looks like this won't be simple to convert to numbers. However, you could categorize flights by duration and examine the frequency of different flight lengths!

# You'll create a "Duration_Category" column in the planes DataFrame. Before you can do this you'll need to create a list of the values you would like to insert into the DataFrame, followed by the existing values that these should be created from.

# Instructions 1/2
# 50 XP
# Instructions 1/2
# 50 XP
# Create a list of categories containing "Short-haul", "Medium", and "Long-haul".
# Create a list of categories
flight_categories = ["Short-haul","Medium","Long-haul"]


# Instructions 2/2
# 15 XP
# Create short_flights, a string to capture values of "0h", "1h", "2h", "3h", or "4h" taking care to avoid values such as "10h".
# Create medium_flights to capture any values between five and nine hours.
# Create long_flights to capture any values from 10 hours to 16 hours inclusive.
# Create a list of categories
flight_categories = ["Short-haul", "Medium", "Long-haul"]

# Create short_flights
short_flights = "^0h|^1h|^2h|^3h|^4h"

# Create medium_flights
medium_flights = "^5h|^6h|^7h|^8h|^9h"

# Create long_flights
long_flights = "10h|11h|12h|13h|14h|15h|16h"




# Adding duration categories
# Now that you've set up the categories and values you want to capture, it's time to build a new column to analyze the frequency of flights by duration!

# The variables flight_categories, short_flights, medium_flights, and long_flights that you previously created are available to you.

# Additionally, the following packages have been imported: pandas as pd, numpy as np, seaborn as sns, and matplotlib.pyplot as plt.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Create conditions, a list containing subsets of planes["Duration"] based on short_flights, medium_flights, and long_flights.
# Create the "Duration_Category" column by calling a function that accepts your conditions list and flight_categories, setting values not found to "Extreme duration".
# Create a plot showing the count of each category.
# Create conditions for values in flight_categories to be created
conditions = [
(planes['Duration'].str.contains(short_flights)),
(planes['Duration'].str.contains(medium_flights)),
(planes['Duration'].str.contains(long_flights))
]

# Apply the conditions list to the flight_categories
planes['Duration_Category'] = np.select(conditions,flight_categories,default='Extreme duration')

# Plot the counts of each category
sns.countplot(data=planes, x='Duration_Category')

plt.show()




# Flight duration
# You would like to analyze the duration of flights, but unfortunately, the "Duration" column in the planes DataFrame currently contains string values.

# You'll need to clean the column and convert it to the correct data type for analysis. seaborn has been imported as sns.

# Instructions 1/4
# 25 XP
# Print the first five values of the "Duration" column.
# Preview the column
print(planes['Duration'].head())


# Instructions 2/4
# 25 XP
# Remove "h" from the column.
# Preview the column
print(planes["Duration"].head())

# Remove the string character
planes["Duration"] = planes["Duration"].str.replace("h","")


# Instructions 3/4
# 25 XP
# Convert the column to float data type.
# Preview the column
print(planes["Duration"].head())

# Remove the string character
planes["Duration"] = planes["Duration"].str.replace("h", "")

# Convert to float data type
planes["Duration"] = planes["Duration"].astype('float')



# Instructions 4/4
# 25 XP
# Plot a histogram of "Duration" values.
# Preview the column
print(planes["Duration"].head())

# Remove the string character
planes["Duration"] = planes["Duration"].str.replace("h", "")

# Convert to float data type
planes["Duration"] = planes["Duration"].astype(float)

# Plot a histogram
sns.histplot(x='Duration',data=planes)
plt.show()


# Adding descriptive statistics
# Now "Duration" and "Price" both contain numeric values in the planes DataFrame, you would like to calculate summary statistics for them that are conditional on values in other columns.


# Instructions 1/3
# 35 XP
# Add a column to planes containing the standard deviation of "Price" based on "Airline".
# Price standard deviation by Airline
planes["airline_price_st_dev"] = planes.groupby("Airline")["Price"].transform(lambda x: x.std())

print(planes[["Airline", "airline_price_st_dev"]].value_counts())



# Calculate the median for "Duration" by "Airline", storing it as a column called "airline_median_duration".
# Median Duration by Airline
planes['airline_median_duration'] = planes.groupby('Airline')['Duration'].transform(lambda x: x.median())

print(planes[["Airline","airline_median_duration"]].value_counts())




# Find the mean "Price" by "Destination", saving it as a column called "price_destination_mean".
# Mean Price by Destination
planes['price_destination_mean'] = planes.groupby('Destination')['Price'].transform(lambda x: x.mean())

print(planes[["Destination","price_destination_mean"]].value_counts())




# Identifying outliers
# You've proven that you recognize what to do when presented with outliers, but can you identify them using visualizations?

# Try to figure out if there are outliers in the "Price" or "Duration" columns of the planes DataFrame.

# matplotlib.pyplot and seaborn have been imported for you as plt and sns respectively.

# Instructions 1/3
# 35 XP
# Plot the distribution of "Price" column from planes.
# Plot a histogram of flight prices
sns.histplot(data=planes,x='Price')
plt.show()



# Instructions 2/3
# 35 XP
# Display the descriptive statistics for flight duration.
# Plot a histogram of flight prices
sns.histplot(data=planes, x="Price")
plt.show()

# Display descriptive statistics for flight duration
print(planes['Duration'].describe())


# Removing outliers
# While removing outliers isn't always the way to go, for your analysis, you've decided that you will only include flights where the "Price" is not an outlier.

# Therefore, you need to find the upper threshold and then use it to remove values above this from the planes DataFrame.

# pandas has been imported for you as pd, along with seaborn as sns.


# Instructions 1/4
# 25 XP
# Find the 75th and 25th percentiles, saving as price_seventy_fifth and price_twenty_fifth respectively.
# Find the 75th and 25th percentiles
price_seventy_fifth = planes['Price'].quantile(0.75)

price_twenty_fifth = planes['Price'].quantile(0.25)

# Calculate the IQR, storing it as prices_iqr.
# Find the 75th and 25th percentiles
price_seventy_fifth = planes["Price"].quantile(0.75)
price_twenty_fifth = planes["Price"].quantile(0.25)

# Calculate iqr
prices_iqr =  price_seventy_fifth - price_twenty_fifth


# Calculate the upper and lower outlier thresholds.
# Find the 75th and 25th percentiles
price_seventy_fifth = planes["Price"].quantile(0.75)
price_twenty_fifth = planes["Price"].quantile(0.25)

# Calculate iqr
prices_iqr = price_seventy_fifth - price_twenty_fifth

# Calculate the thresholds
upper = price_seventy_fifth + (1.5 * prices_iqr)
lower = price_twenty_fifth - (1.5 * prices_iqr)



# Remove the outliers from planes.
# Find the 75th and 25th percentiles
price_seventy_fifth = planes["Price"].quantile(0.75)
price_twenty_fifth = planes["Price"].quantile(0.25)

# Calculate iqr
prices_iqr = price_seventy_fifth - price_twenty_fifth

# Calculate the thresholds
upper = price_seventy_fifth + (1.5 * prices_iqr)
lower = price_twenty_fifth - (1.5 * prices_iqr)

# Subset the data
planes = planes[(planes['Price'] > lower) & (planes['Price'] < upper)]

print(planes["Price"].describe())

