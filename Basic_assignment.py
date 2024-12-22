# Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.
import pandas as pd
data = [4, 8, 15, 16, 23,42]
series=pd.Series(data)
print(series)
print("\n")

# Q2. Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the variable print it.
data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
series = pd.Series(data_list)
print(series)
print("\n")

# Q3. Create a Pandas DataFrame that contains the following data:
data_frame={
  "Name":["Alice","Bob","Claire"],
  "Age":[25,30,27],
  "Gender":["Female","Male","Female"]
}
df=pd.DataFrame(data_frame)
print(df)
print("\n")

# Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.
print("DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.","\n","Pandas Series : Pandas Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.")
data = [10, 20, 30, 40, 50]
series2 = pd.Series(data)
print("Pandas Series:")
print(series2)
print("\n")
print("Pandas DataFrame : pandas DataFrame is a way to represent and work with tabular data. It can be seen as a table that organizes data into rows and columns, making it a two-dimensional data structure.")
# Creating a Pandas DataFrame
data_dict = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data_dict)
print("\nPandas DataFrame:")
print(df)
print("\n")

# Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Can you give an example of when you might use one of these functions?
print("1. Viewing and Inspecting Data head(n): Displays the first n rows. tail(n): Displays the last n rows. info(): Provides a summary of the DataFrame. describe(): Generates statistical summaries for numerical columns.","\n","2. Selection and Filtering loc[]: Access rows and columns by label. iloc[]: Access rows and columns by integer indices. query(): Filter data using conditions.","\n")
df.head()
df.tail()
df.info()

# Q6. Which of the following is mutable in nature Series, DataFrame, Panel?
# Answer : Both Series and DataFrame in Pandas are mutable in nature.

# Q7. Create a DataFrame using multiple Series. Explain with an example.
Student_Name = pd.Series(["Vishal", "Guddu", "Vikash", "Samarth"])
Student_ages = pd.Series([19,21,20,7])
Student_cities = pd.Series(["Chandigarh", "Sarai", "Patna", "Garahi"])
data = pd.DataFrame({
    "Name": Student_Name,
    "Age": Student_ages,
    "City": Student_cities
})
print(data)
