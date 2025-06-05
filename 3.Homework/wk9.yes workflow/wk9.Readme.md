## Assignment #6: Data Cleaning with Python Pandas

Hello everyone, welcome to the "Python & pandas" assignment! 

In this notebook, you will do the following:

Section 0: Load a dataset and get an overview
Section 1: Prepare a dataset using general operations
Section 2: Detect outliers
Section 3: Detect and remove errors (datetime and text strings)
Section 4: Deal with missing values
Section 5: Discovery of integrity constraint violations using pandas 

## External reference that might be useful:
Mini-Tutorial: [10 minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

NOTE:
You should remove the quotes ("YOUR CODE HERE") when working with the code.
Please execute the notebook cells IN ORDER and DO NOT SKIP STEPS

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn')
```

# Section 0: Load the Dataset
**Dataset Description:** The original dataset is derived from New York City Airbnb Open Data [source](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data).
**Context:** Since 2008, guests and hosts have used Airbnb to expand on traveling possibilities and present more unique, personalized way of experiencing the world. This dataset describes the listing activity and metrics in NYC, NY for 2019.
**Content:** This data file includes all needed information to find out more about hosts, geographical availability, necessary metrics to make predictions and draw conclusions.
**Acknowledgements:** This public dataset is part of Airbnb, and the original source can be found on this [website](http://insideairbnb.com/).

```
# Load a CSV file as a data frame (df) using pandas
# Parameters: filepath_or_buffer; use separator: default "," 
df = pd.read_csv('NYC-Airbnb-Visible-Dirty.csv', sep=',')

# Use the head() function to see the table schema and the first 5 rows:
df.head()

# Hey, look: This is how you call on a specific column room_type in a dataframe!" 
# Note how you also learn how many rows there are ..
df['room_type']

# value_counts(): Return a Series containing counts of unique values. 
# value_counts(): https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html
# This function is somewhat similar to "Text Facet" in OpenRefine
df['neighbourhood'].value_counts()
```

# Section 1: Prepare Data with General Operations
In this section, we will learn how to use Python functions to:
1. trim leading and trailing whitespaces
2. perform uppercase/lowercase conversions

These general operations can be used to transform the data into a more consistent, canonical representation, in preparation for the actual process of deduplication; cf. Koumarelas, I., Jiang, L., & Naumann, F. (2020), Data Preparation for Duplicate Detection.

1.1 Trim Leading and Trailing Whitespaces with function strip() : [Documentation](https://pandas.pydata.org/pandas-docs/version/1.2.4/reference/api/pandas.Series.str.strip.html)

## [6 points] Question 1:

##### Create two new columns name_trim and host_name_trim by trimming leading and trailing whitespaces on column name, and host_name, respectively. Hint: use strip() from str.

```
def q1(df):
#     df['name_trim'] = "YOUR CODE HERE"
#     df['host_name_trim'] = "YOUR CODE HERE"
    df['name_trim'] = df['name'].str.strip()
    df['host_name_trim'] = df['host_name'].str.strip()
```

```
# Self-Testing Time [no points assigned]: 
# This works as an instant feedback to check if the function q1() performs well
# Create a new dataframe df_trim_test with four columns: `name_trim`, `name`, `host_name_trim`, and `host_name`
q1(df)
df_trim_test = df[
                 ['name_trim', 'name', 'host_name_trim', 'host_name']
    ]
df_trim_test.head()
```

# 1.2 Uppercase values with function upper(): Documentation.
Data quality issues analysis: The values in column name vary in their format, i.e. some values are uppercase only, some are lowercase only, some values are mixed uppercase and lowercase.
[2 points] Question 2:
Create a new column name_upper by applying function upper() on column name_trim

```
def q2(df):
#     df['name_upper'] = "YOUR CODE HERE"
    df['name_upper'] = df['name_trim'].str.upper()
```

```
# Self-Testing Time [no points assigned]: 
# This works as an instant feedback to check if the function q2() performs well
# Create a new dataframe df_upper_test with two columns: `name_trim` and `name_upper`
q2(df)
df_upper_test = df[
                 ['name_trim', 'name_upper']
    ]
df_upper_test.head()
```

# Section 2: Outlier Detection
- Let's first look at the data distribution of the values in column price.
- We can see that approximately 99% of the values are below 162.5 (run the cells below and see how we compute 162.5). There are few data points that are very high and can be considered an outliers. Most machine learning models are heavily impacted by outliers, hence we often need to identify and deal with such outliers.
- The following figure should help you understand outliers. It compares a normal distribution with a boxplot. A boxplot considers a point an outlier if it falls outside of the 1.5*interquantile range.

```
df.price.describe()
```

Explanation: Values above 162.5 are considered outliers. Below 162.5, we have approximately 24.65*2+50 = 99.3 % of data. [external reference](https://www.whatissixsigma.net/box-plot-diagram-to-identify-outliers/)

```
# Below is the boxplot for the price column. It's a fairly slim box and we see that there are many outliers here!
plt.figure(figsize=[18,5])
plt.boxplot(df.price, vert=False)
plt.xlabel('price')
plt.show()
```

## 2.1 Winsorize - clipping extreme values
As you probably know, means, standard deviations, correlations, mean squared errors and other statistics and models based on these are highly sensitive to outliers.
One way of dealing with outliers is by using winsorization. This simply means capping data values at certain thresholds, based on the distribution of data. The function winsorize() from Scipy: [Reference](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mstats.winsorize.html)
Here you can learn more about this technique: https://en.wikipedia.org/wiki/Winsorizing
Below is an example quoated from the wikipedia page.

```
# Source: https://en.wikipedia.org/wiki/Winsorizing
# The code below performs 90% winsorization on the data contained in the python list.
# Observe that large values such as 1053, were replaced with 101, and -40 was replaced to -5.
from scipy.stats.mstats import winsorize
winsorize([92, 19, 101, 58, 1053, 91, 26, 78, 10, 13, -40, 101, 86, 85, 15, 89, 89, 28, -5, 41], limits=[0.05, 0.05])
```

**[10 points] Question 3:**
Winsorize column price with 99% winsorization.
Hints:
Use the winsorize() function from above ([reference](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mstats.winsorize.html)).
The example given above was a 90% winsorization. You need to tweak the paratermer limits with 99% winsorization instead.

```
from scipy.stats.mstats import winsorize
def q3(df):
#     df['price_winsorized'] = "YOUR CODE HERE"      
    df['price_winsorized'] = winsorize(df['price'], limits=[0.005, 0.005])
```

```
# Visualizing the new column price after 99% winsorization
plt.figure(figsize=[18,5])
plt.boxplot(df.price_winsorized, vert=False)
plt.xlabel('price_winsorized')
plt.show()
```

```
# Visualize the new price column
# We can observe that most of the data lies below 400
plt.figure(figsize=[18,8])
plt.subplot(211)
plt.boxplot(df.minimum_nights, vert=False)
plt.xlabel('minimum_nights')
plt.title('boxplot minimum nights column')

plt.subplot(212)
plt.scatter(df.minimum_nights, df.price_winsorized)
plt.xlabel('minimum nights')
plt.ylabel('price')
plt.title('minimum nights vs price')
plt.tight_layout()
# plt.show()
```
Note: Suppose we investigated data points with minimum nights above 400 and found that these observations do not have the correct price mentioned and hence do not follow the trend. We may then decide to drop these points, considering them as outliers.

[10 points] Question 4:
Create a new data frame df_wt_outliers by dropping observations whose values in column minimum_nights are greater or equal to 400.
Hint: Article for [reference](https://www.geeksforgeeks.org/drop-rows-from-the-dataframe-based-on-certain-condition-applied-on-a-column/)

```
def q4(df):
#     df_wt_outliers = "YOUR CODE HERE"
    df_wt_outliers = df[df['minimum_nights'] < 400]
    return df_wt_outliers  
    
```

# Section 3: Detect and remove errors (datetime and text strings)
In the following, we will go over Python methods for handling two types of errors in the Airbnb dataset:
- Handling Datetime errors
- Handling Typos

3.1 Handling Datetime errors
Data type
Let's first check the data types of the current dataset. DataFrame.info() method prints a concise summary of the dataframe, including column names, Non-Null value count and data types. Here is a sample list of data types, supported by Pandas:
float float64
int int64
datetime datetime64[ns]
string object
Note: Pandas stores the column with mixed data types as 'object' by default. Reference: [link](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html)

```
df.info(verbose=True)
```

#
Datetime
Data cleaning often includes steps to convert data into different formats, so it can be used for various analysis purposes.
Reviewing the output above, we find that the data type of column last_review is object. However, column last_review indicates the date when an Airbnb listing received lastest review. Therefore, we want to convert the column last_review to a datetime type and check if it contains any issues. (Reference: Docs)
We will use the .to_datetime(arg, format='%m/%d/%y', errors='coerce') function in pandas to convert the column last_review to a standard datetime format.
arg: denotes the input column to be converted
format: identifies and limits the default format in the raw data. In the airbnb dataset, we can find the string in the 'last_review' column, e.g. "10/19/18" is in the "%m/%d/%y" format
errors='coerce': turns any strings that violates the format into Null value.

## Step 1: Convert the data type of column last_review to datetime
Convert column last_review to datetime format, replace dates that are not in '%m/%d/%y' format as null (NaT), and save it as new_last_review.


```
def q5(df):
    df['new_last_review'] = pd.to_datetime(df['last_review'], format='%m/%d/%y', errors='coerce')
    
```

```
# Return the dates that cannot be parsed by the defined format '%m/%d/%y' 
# and have been converted to NaT,
# e.g. the month is out of the range of [1,12].
df['last_review'][~df.last_review.isna() & df['new_last_review'].isna()]
```

##
Step 2: Extract year, month, day from new_last_review Series

```
df["year"] = df['new_last_review'].dt.year
df["month"] = df['new_last_review'].dt.month
df["day"] = df['new_last_review'].dt.day

df[["last_review","year","month","day"]].head(5)
```

###
Use DataFrame.replace() to correct "Mannhattan" and "Manhattann" to "Manhattan", and "Brooklyyn" to "Brooklyn", respectively. Save the new values in a new column neighbourhood_group_new. See also pandas.DataFrame.replace

```
def q6(df):
#     df['neighbourhood_group_new'] = "YOUR CODE HERE"
    df['neighbourhood_group_new'] = df['neighbourhood_group'].replace({
    'Mannhattan': 'Manhattan',
    'Manhattann': 'Manhattan',
    'Brooklyyn': 'Brooklyn'
})
```

## Section 4: Dealing with missing values
In this section, you will learn about detecting missing values (and the difference between NA and NULL), different types of missing values, and simple methods to deal with missing values.

**4.1 Missing Values Detection**
Goal: learn how to use pandas to detect missing values in columns.

Calculate the percentage of missing values on the columns neighbourhood and number_of_reviews.

'''
def q7(df):
#     neighbourhood_missing_ptg = "YOUR CODE HERE"
#     number_reviews_missing_ptg = "YOUR CODE HERE"
    neighbourhood_missing_ptg = df['neighbourhood'].isnull().mean() * 100
    number_reviews_missing_ptg = df['number_of_reviews'].isnull().mean() * 100
    
    return neighbourhood_missing_ptg, number_reviews_missing_ptg
'''
