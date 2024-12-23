# Importing DateTime data
# You'll now work with the entire divorce dataset! The data describes Mexican marriages dissolved between 2000 and 2015. It contains marriage and divorce dates, education level, birthday, income for each partner, and marriage duration, as well as the number of children the couple had at the time of divorce.

# The column names and data types are as follows:

# divorce_date          object
# dob_man               object
# education_man         object
# income_man           float64
# dob_woman             object
# education_woman       object
# income_woman         float64
# marriage_date         object
# marriage_duration    float64
# num_kids             float64
# It looks like there is a lot of date information in this data that is not yet a DateTime data type! Your task is to fix that so that you can explore patterns over time.

# pandas has been imported as pd.

# Instructions
# 100 XP
# Import divorce.csv, saving as a DataFrame, divorce; indicate in the import function that the divorce_date, dob_man, dob_woman, and marriage_date columns should be imported as DateTime values.
# Import divorce.csv, parsing the appropriate columns as dates in the import
divorce =  pd.read_csv('divorce.csv',parse_dates=['divorce_date', 'dob_man', 'dob_woman', 'marriage_date'])


print(divorce.dtypes)



# Updating data type to DateTime
# Now, the divorce DataFrame has been loaded for you, but one column is stored as a string that should be DateTime data. Which one is it? Once you've identified the column, you'll update it so that you can explore it more closely in the next exercise.

# pandas has been imported as pd.

# Instructions 1/2
# 50 XP
# Question
# Which of the columns in the divorce DataFrame has not been updated to a DateTime data type but should be?

# Possible answers


# divorce_date

# -> true ans: marriage_date

# education_woman

# num_kids


# Instructions 2/2
# 50 XP
# Convert the marriage_date column of the divorce DataFrame to DateTime values.
# Convert the marriage_date column to DateTime values
divorce["marriage_date"] = pd.to_datetime(divorce['marriage_date'])


# Visualizing relationships over time
# Now that your date data is saved as DateTime data, you can explore patterns over time! Does the year that a couple got married have a relationship with the number of children that the couple has at the time of divorce? Your task is to find out!

# The divorce DataFrame (with all dates formatted as DateTime data types) has been loaded for you. pandas has been loaded as pd, matplotlib.pyplot has been loaded as plt, and Seaborn has been loaded as sns.

# Instructions 1/2
# 50 XP
# Define a column called marriage_year, which contains just the year portion of the marriage_date column.
# Define the marriage_year column
divorce["marriage_year"] = divorce['marriage_date'].dt.year


# Instructions 2/2
# 50 XP
# Create a line plot showing the average number of kids a couple had during their marriage, arranged by the year that the couple got married.

# Define the marriage_year column
divorce["marriage_year"] = divorce["marriage_date"].dt.year

# Create a line plot showing the average number of kids by year
sns.lineplot(data=divorce,x='marriage_year',y='num_kids')
plt.show()




# Interpreting a heatmap
# Which of the below statements is correct regarding the relationships between variables in the divorce DataFrame?

# The divorce DataFrame has been loaded for you so that you can explore it in the shell. pandas has been loaded as pd, matplotlib.pyplot has been loaded as plt, and Seaborn has been loaded as sns.

# Instructions
# 50 XP
# Possible answers


# marriage_duration is strongly positively correlated with marriage_month.

# The correlation between num_kids and income_man is stronger than the correlation between num_kids and marriage_duration.

# A later marriage_year causes a lower number of children, represented by num_kids.

# -> true ans: A later marriage_year is correlated with having fewer children.




# Visualizing variable relationships
# In the last exercise, you may have noticed that a longer marriage_duration is correlated with having more children, represented by the num_kids column. The correlation coefficient between the marriage_duration and num_kids variables is 0.45.

# In this exercise, you'll create a scatter plot to visualize the relationship between these variables. pandas has been loaded as pd, matplotlib.pyplot has been loaded as plt, and Seaborn has been loaded as sns. The dataset name is divorce.

# Instructions
# 100 XP
# Create a scatterplot showing marriage_duration on the x-axis and num_kids on the y-axis.
# Create the scatterplot
sns.scatterplot(data=divorce,x='marriage_duration',y='num_kids')
plt.show()

# Categorical data in scatter plots
# In the video, we explored how men's education and age at marriage related to other variables in our dataset, the divorce DataFrame. Now, you'll take a look at how women's education and age at marriage relate to other variables!

# Your task is to create a scatter plot of each woman's age and income, layering in the categorical variable of education level for additional context.

# The divorce DataFrame has been loaded for you, and woman_age_marriage has already been defined as a column representing an estimate of the woman's age at the time of marriage. pandas has been loaded as pd, matplotlib.pyplot has been loaded as plt, and Seaborn has been loaded as sns.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Create a scatter plot that shows woman_age_marriage on the x-axis and income_woman on the y-axis; each data point should be colored based on the woman's level of education, represented by education_woman.

# Create the scatter plot
sns.scatterplot(x='woman_age_marriage',y='income_woman',hue='education_woman',data=divorce)
plt.show()

# Exploring with KDE plots
# Kernel Density Estimate (KDE) plots are a great alternative to histograms when you want to show multiple distributions in the same visual.

# Suppose you are interested in the relationship between marriage duration and the number of kids that a couple has. Since values in the num_kids column range only from one to five, you can plot the KDE for each value on the same plot.

# The divorce DataFrame has been loaded for you. pandas has been loaded as pd, matplotlib.pyplot has been loaded as plt, and Seaborn has been loaded as sns. Recall that the num_kids column in divorce lists only N/A values for couples with no children, so you'll only be looking at distributions for divorced couples with at least one child.

# Instructions 1/3
# 35 XP
# Instructions 1/3
# 35 XP
# Create a KDE plot that shows marriage_duration on the x-axis and a different colored line for each possible number of children that a couple might have, represented by num_kids.
# Create the KDE plot
sns.kdeplot(x='marriage_duration',hue='num_kids',data=divorce)
plt.show()

# Instructions 2/3
# 35 XP
# Notice that the plot currently shows marriage durations less than zero; update the KDE plot so that marriage duration cannot be smoothed past the extreme data points.
# Update the KDE plot so that marriage duration can't be smoothed too far
sns.kdeplot(data=divorce, x="marriage_duration", hue="num_kids",  cut=0)
plt.show()

# Instructions 3/3
# 30 XP
# Update the code for the KDE plot from the previous step to show a cumulative distribution function for each number of children a couple has.
# Update the KDE plot to show a cumulative distribution function
sns.kdeplot(data=divorce, x="marriage_duration", hue="num_kids", cut=0, cumulative=True)
plt.show()