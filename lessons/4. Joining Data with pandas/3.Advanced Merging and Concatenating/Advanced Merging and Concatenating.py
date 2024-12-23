# Performing an anti join
# In our music streaming company dataset, each customer is assigned an employee representative to assist them. In this exercise, filter the employee table by a table of top customers, returning only those employees who are not assigned to a customer. The results should resemble the results of an anti join. The company's leadership will assign these employees additional training so that they can work with high valued customers.

# The top_cust and employees tables have been provided for you.

# Instructions 3/3
# 30 XP
# Subset the employees table and select those rows where the srid is in the variable srid_list and print the results.

# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid', 
                                 how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
print(employees[employees['srid'].isin(srid_list)])


# Performing a semi join
# Some of the tracks that have generated the most significant amount of revenue are from TV-shows or are other non-musical audio. You have been given a table of invoices that include top revenue-generating items. Additionally, you have a table of non-musical tracks from the streaming service. In this exercise, you'll use a semi join to find the top revenue-generating non-musical tracks.

# The tables non_mus_tcks, top_invoices, and genres have been loaded for you.

# Instructions
# 100 XP
# Merge non_mus_tcks and top_invoices on tid using an inner join. Save the result as tracks_invoices.
# Use .isin() to subset the rows of non_mus_tcks where tid is in the tid column of tracks_invoices. Save the result as top_tracks.
# Group top_tracks by gid and count the tid rows. Save the result to cnt_by_gid.
# Merge cnt_by_gid with the genres table on gid and print the result.


# Merge the non_mus_tck and top_invoices tables on tid
tracks_invoices = non_mus_tcks.merge(top_invoices, on='tid')

# Use .isin() to subset non_mus_tcsk to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':'count'})

# Merge the genres table to cnt_by_gid on gid and print
print(cnt_by_gid.merge(genres, on='gid'))


# Concatenation basics
# You have been given a few tables of data with musical track info for different albums from the metal band, Metallica. The track info comes from their Ride The Lightning, Master Of Puppets, and St. Anger albums. Try various features of the .concat() method by concatenating the tables vertically together in different ways.

# The tables tracks_master, tracks_ride, and tracks_st have loaded for you.

# Instructions 3/3
# 40 XP
# Concatenate tracks_master, tracks_ride, and tracks_st, in that order, setting sort to True.
# Concatenate the tracks
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st], sort=True)
print(tracks_from_albums)


# Concatenate tracks_master, tracks_ride, and tracks_st, where the index goes from 0 to n-1.
# Concatenate the tracks so the index goes from 0 to n-1
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st], ignore_index=True, sort=True)
print(tracks_from_albums)


# Concatenate tracks_master, tracks_ride, and tracks_st, showing only columns that are in all tables.
# Concatenate the tracks, show only columns names that are in all tables
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st], join='inner', sort=True)
print(tracks_from_albums)



# Concatenating with keys
# The leadership of the music streaming company has come to you and asked you for assistance in analyzing sales for a recent business quarter. They would like to know which month in the quarter saw the highest average invoice total. You have been given three tables with invoice data named inv_jul, inv_aug, and inv_sep. Concatenate these tables into one to create a graph of the average monthly invoice total.

# Instructions
# 100 XP
# Concatenate the three tables together vertically in order with the oldest month first, adding '7Jul', '8Aug', and '9Sep' as keys for their respective months, and save to inv_jul_thr_sep.
# Use the .agg() method to find the average of the total column from the grouped invoices.
# Create a bar chart of avg_inv_by_month.

# Concatenate the tables and add keys
inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep], 
                            keys=['7Jul','8Aug','9Sep'])

# Group the invoices by the index keys and find avg of the total column
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})

# Bar plot of avg_inv_by_month
avg_inv_by_month.plot(kind='bar')
plt.show()


# Validating a merge
# You have been given 2 tables, artists, and albums. Merge them using artists.merge(albums, on='artid').head(), adjusting the validate argument to determine which statement is False.

# Instructions
# 50 XP
# Possible answers


# You can use 'many_to_many' without an error, since there is a duplicate key in one of the tables.

# You can use 'one_to_many' without error, since there is a duplicate key in the right table.

# -> true ans: You can use 'many_to_one' without an error, since there is a duplicate key in the left table.


# Concatenate and merge to find common songs
# The senior leadership of the streaming service is requesting your help again. You are given the historical files for a popular playlist in the classical music genre in 2018 and 2019. Additionally, you are given a similar set of files for the most popular pop music genre playlist on the streaming service in 2018 and 2019. Your goal is to concatenate the respective files to make a large classical playlist table and overall popular music table. Then filter the classical music table using a semi join to return only the most popular classical music tracks.

# The tables classic_18, classic_19, and pop_18, pop_19 have been loaded for you. Additionally, pandas has been loaded as pd.

# Instructions 2/2
# 50 XP
# Instructions 2/2
# 50 XP
# With classic_18_19 on the left, merge it with pop_18_19 on tid using an inner join.
# Use .isin() to filter classic_18_19 where tid is in classic_pop.


# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)

# Merge classic_18_19 with pop_18_19
classic_pop = classic_18_19.merge(pop_18_19, on='tid')

# Using .isin(), filter classic_18_19 rows where tid is in classic_pop
popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]

# Print popular chart
print(popular_classic)