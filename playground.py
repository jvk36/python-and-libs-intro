import numpy as np
import pandas as pd

a = [1, 2, 3] + [4, 5, 6]
print(a)
a = np.array([1, 2, 3]) + np.array([4, 5, 6])
print(a)
print(type(a))
print(a.dtype)

series = pd.Series([1, 2, 3, 4, 5])
print(series)
series.reset_index()
print(series)
print(series.dtype)

dataframe = pd.DataFrame({"Name": ["John", "Jane"], "Age": [20, 21]})
print(dataframe.index.dtype)
dataframe.loc[len(dataframe)] = ['Jessica', 25]
print(dataframe.Age.idxmax())

dataframe.loc[len(dataframe)] = {'Name': 'Joe'}
print(dataframe.head())

dataframe["Country"] = "USA"
pivoted = dataframe.pivot(index='Country', columns='Name', values='Age')
print(pivoted.head())

concat_df = pd.concat([dataframe, dataframe])
print(concat_df)

merged_df = pd.merge(dataframe, dataframe)
print(merged_df)

# join_df = dataframe.join(dataframe, on="Name")
# print(join_df)
