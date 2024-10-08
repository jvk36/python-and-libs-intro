import pandas


student_dict = {
    "student": ["Angela", "James", "lily"],
    "score": [56, 78, 33],
}

df = pandas.DataFrame(student_dict)
print(df)
# iterate over the student and score columns
for (key, value) in df.items():
    print(type(value)) # it is a series containing a column values - ("Angela", "James", "lily") or (56, 78, 33) in this case
    print(value)

# to iterate over the rows by using index instead, use iterrow
for (index, row) in df.iterrows():
    print(type(row)) # it is a series containing row values - ("Angela", 56), ("James", 78) or ("lily", 33) in this case
    print(row)
    print(row.student)
    print(row.score)
