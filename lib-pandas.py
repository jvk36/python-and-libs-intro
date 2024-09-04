import pandas as pd

# CREATING SERIES AND DATAFRAMES
print("\nCREATING SERIES AND DATAFRAMES EXAMPLE:\n")
series = pd.Series([1, 2, 3, 4, 5])
print(f"series = pd.Series([1, 2, 3, 4, 5]):\n{series}")
print(f"Datatypes of the elements in the series: series.dtype: {series.dtype}")
dataframe = pd.DataFrame({"Name": ["John", "Jane"], "Age": [20, 21], "City": ["NY", "SFO"]})
print(f'\ndataframe = pd.DataFrame({{"Name": ["John", "Jane"], "Age": [20, 21]}}):\n')
print(dataframe)
print(f"\nDatatypes of the columns in the dataframe: dataframe.dtypes: \n\n{dataframe.dtypes}")
print(f"\nDatatype of the index of the dataframe: dataframe.index.dtype: {dataframe.index.dtype}")

# ACCESSOR OPERATIONS:
print("\nACCESSOR OPERATIONS EXAMPLES:\n")
print(f"First 5 rows: dataframe.head():\n{dataframe.head()}")  # First 5 rows
print(f"\nLast 5 rows: dataframe.tail():\n{dataframe.tail()}")  # Last 5 rows
print(f"\nSummary of DataFrame: dataframe.info():")  # Summary of DataFrame
print(dataframe.info())
print(f"\nStats of DataFrame: dataframe.describe():")  # Stats of DataFrame
print(dataframe.describe())
print("\nListing Columns:")
print(f"dataframe.columns: {dataframe.columns}")
print("\nListing the Index:")
print(f"dataframe.index: {dataframe.index}")
print("\nGetting name and age of the oldest person and their index:")
print(f"dataframe.Name.iloc[dataframe.Age.idxmax()]: {dataframe.Name.iloc[dataframe.Age.idxmax()]}")
print(f"dataframe.Age.max(): {dataframe.Age.max()}, dataframe.Age.idxmax(): {dataframe.Age.idxmax()}")
print("\nAccessing a Cell:")
print(f"dataframe['Name'][1]: {dataframe['Name'][1]}")
print(f"\nSelecting Columns: dataframe[['Name', 'City']]:\n\n{dataframe[['Name', 'City']]}")
print("\nAccessing a row using the index:")
print(f"dataframe.loc[1]:\n\n{dataframe.loc[1]}")
print("\nAccessing row(s) using [indexes]:")
print(f"dataframe.loc[[0, 1]]:\n\n{dataframe.loc[[0, 1]]}")
print("\nFiltering Rows:")
young_people = dataframe[dataframe['Age'] < 21]
print(f"young_people = dataframe[dataframe['Age'] < 21]: \n{young_people}")

# Add a new column
print("\nADD A NEW COLUMN:\n")
dataframe["Country"] = "USA"
print('dataframe["Country"] = "USA": dataframe.head():\n')
print(dataframe.head())

# Add a new row
print("\nADD A NEW ROW:\n")
dataframe.loc[len(dataframe)] = ["Jessica", 25, "SFO", "USA"]
print('dataframe.loc[len(dataframe)] = ["Jessica", 25, "SFO", "USA"]: dataframe.head():\n')
print(dataframe.head())

# Grouping and Aggregation
print("\nGROUPING AND AGGREGATION:\n")
average_age_by_city = dataframe.groupby('City')['Age'].mean()
print("average_age_by_city = dataframe.groupby('City')['Age'].mean()")
print(f"average_age_by_city:\n\n{average_age_by_city}")
counts_by_city = dataframe.groupby('City').count()
print("counts_by_city = dataframe.groupby('City').count()")
print(f"counts_by_city:\n\n{counts_by_city}")

# Sorting Values
print("\nSORTING VALUES EXAMPLE:\n")
df_sorted = dataframe.sort_values(by='Age', ascending=False)
print("df_sorted = dataframe.sort_values(by='Age', ascending=False): df_sorted")
print(df_sorted)

# Handling Missing Data
print("\nHANDLING MISSING VALUES:\n")
dataframe.loc[len(dataframe)] = {'Name': 'Joe'}
# Count the # of missing values per column
print(f"Count the # of missing values per column: dataframe.isna().sum(): {dataframe.isna().sum()}")
# Count the total number of missing values
print(f"Count the total # of missing values: dataframe.isna().sum(): {dataframe.isna().values.sum()}")
# drop the na values from the dataframe
print("\nDrop na values from the dataframe:")
dataframe = dataframe.dropna()
print(f"dataframe = dataframe.dropna(): dataframe:\n{dataframe}")
# replace na values with zeros in the dataframe
print("\nReplace na values with zeros in the dataframe:")
dataframe.loc[len(dataframe)] = {'Name': 'Joe'}
dataframe = dataframe.fillna(0)
print(f"dataframe = dataframe.fillna(0): dataframe:\n{dataframe}")

# Pivoting Dataframes
print("\nPIVOTING DATAFRAMES:\n")
pivoted = dataframe.pivot(index='Country', columns='Name', values='Age')
print("pivoted = dataframe.pivot(index='Country', columns='Name', values='Age')")
print(f"privoted:\n{pivoted}")

# Concatenation and Merging of Dataframes
print("\nCONCATENATION AND MERGING OF DATAFRAMES:\n")
df_concat = pd.concat([dataframe, dataframe])
print("df_concat = pd.concat([dataframe, dataframe]):")
print(df_concat)
merged_df = pd.merge(dataframe, dataframe)
print("merged_df = pd.merge(dataframe, dataframe):")
print(merged_df)





