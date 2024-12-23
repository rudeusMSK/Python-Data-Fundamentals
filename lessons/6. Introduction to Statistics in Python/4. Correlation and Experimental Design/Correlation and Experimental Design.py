# Relationships between variables
# In this chapter, you'll be working with a dataset world_happiness containing results from the 2019 World Happiness Report. The report scores various countries based on how happy people in that country are. It also ranks each country on various societal aspects such as social support, freedom, corruption, and others. The dataset also includes the GDP per capita and life expectancy for each country.

# In this exercise, you'll examine the relationship between a country's life expectancy (life_exp) and happiness score (happiness_score) both visually and quantitatively. seaborn as sns, matplotlib.pyplot as plt, and pandas as pd are loaded and world_happiness is available.

# Instructions 1/4
# 25 XP
# Create a scatterplot of happiness_score vs. life_exp (without a trendline) using seaborn.
# Show the plot.


# Instructions 2/4
# 25 XP
# Create a scatterplot of happiness_score vs. life_exp with a linear trendline using seaborn, setting ci to None.
# Show the plot.
# Create scatterplot of happiness_score vs life_exp with trendline
sns.lmplot(x='life_exp', y='happiness_score', data=world_happiness, ci=None)

# Show plot
plt.show()


# Instructions 3/4
# 25 XP
# Question
# Based on the scatterplot, which is most likely the correlation between life_exp and happiness_score?

# Possible answers


# 0.3

# -0.3

# -> true ans: 0.8

# -0.8


# Instructions 4/4
# 25 XP
# Calculate the correlation between life_exp and happiness_score. Save this as cor.
# Create scatterplot of happiness_score vs life_exp with trendline
sns.lmplot(x='life_exp', y='happiness_score', data=world_happiness, ci=None)

# Show plot
plt.show()

# Correlation between life_exp and happiness_score
cor = world_happiness['life_exp'].corr(world_happiness['happiness_score'])

print(cor)



# What can't correlation measure?
# While the correlation coefficient is a convenient way to quantify the strength of a relationship between two variables, it's far from perfect. In this exercise, you'll explore one of the caveats of the correlation coefficient by examining the relationship between a country's GDP per capita (gdp_per_cap) and happiness score.

# pandas as pd, matplotlib.pyplot as plt, and seaborn as sns are imported, and world_happiness is loaded.

# Instructions 1/3
# 35 XP
# Create a seaborn scatterplot (without a trendline) showing the relationship between gdp_per_cap (on the x-axis) and life_exp (on the y-axis).
# Show the plot
# Scatterplot of gdp_per_cap and life_exp
sns.scatterplot(x='gdp_per_cap', y='life_exp', data=world_happiness)

# Show plot
plt.show()



# Instructions 2/3
# 35 XP
# Calculate the correlation between gdp_per_cap and life_exp and store as cor.

# Scatterplot of gdp_per_cap and life_exp
sns.scatterplot(x='gdp_per_cap', y='life_exp', data=world_happiness)

# Show plot
plt.show()
  
# Correlation between gdp_per_cap and life_exp
cor = world_happiness['gdp_per_cap'].corr(world_happiness['life_exp'])

print(cor)

# Instructions 3/3
# 30 XP
# Question
# The correlation between GDP per capita and life expectancy is 0.7. Why is correlation not the best way to measure the relationship between these two variables?

# Possible answers


# Correlation measures how one variable affects another.

# -> true ans: Correlation only measures linear relationships.

# Correlation cannot properly measure relationships between numeric variables.




# Transforming variables
# When variables have skewed distributions, they often require a transformation in order to form a linear relationship with another variable so that correlation can be computed. In this exercise, you'll perform a transformation yourself.

# pandas as pd, numpy as np, matplotlib.pyplot as plt, and seaborn as sns are imported, and world_happiness is loaded.

# Instructions 1/2
# 50 XP
# Create a scatterplot of happiness_score versus gdp_per_cap and calculate the correlation between them.
# Scatterplot of happiness_score vs. gdp_per_cap
sns.scatterplot(x='gdp_per_cap', y='happiness_score', data=world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness['gdp_per_cap'].corr(world_happiness['happiness_score'])
print(cor)


# Add a new column to world_happiness called log_gdp_per_cap that contains the log of gdp_per_cap.
# Create a seaborn scatterplot of happiness_score versus log_gdp_per_cap.
# Calculate the correlation between log_gdp_per_cap and happiness_score.
# Create log_gdp_per_cap column
world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])

# Scatterplot of happiness_score vs. log_gdp_per_cap
sns.scatterplot(x='log_gdp_per_cap', y='happiness_score', data=world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness['log_gdp_per_cap'].corr(world_happiness['happiness_score'])
print(cor)



# Does sugar improve happiness?
# A new column has been added to world_happiness called grams_sugar_per_day, which contains the average amount of sugar eaten per person per day in each country. In this exercise, you'll examine the effect of a country's average sugar consumption on its happiness score.

# pandas as pd, matplotlib.pyplot as plt, and seaborn as sns are imported, and world_happiness is loaded.

# Instructions 1/2
# 50 XP
# Create a seaborn scatterplot showing the relationship between grams_sugar_per_day (on the x-axis) and happiness_score (on the y-axis).
# Calculate the correlation between grams_sugar_per_day and happiness_score.
# Scatterplot of grams_sugar_per_day and happiness_score
sns.scatterplot(x='grams_sugar_per_day', y='happiness_score', data=world_happiness)
plt.show()

# Correlation between grams_sugar_per_day and happiness_score
cor = world_happiness['grams_sugar_per_day'].corr(world_happiness['happiness_score'])
print(cor)

# Instructions 2/2
# 50 XP
# Question
# Based on this data, which statement about sugar consumption and happiness scores is true?

# Possible answers


# Increased sugar consumption leads to a higher happiness score.

# Lower sugar consumption results in a lower happiness score

# -> true ans: Increased sugar consumption is associated with a higher happiness score.

# Sugar consumption is not related to happiness.





















