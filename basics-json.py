import json

# ENCODING python to JSON - json.dumps(): Converts a Python object into a JSON string.
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(data)
print(json_string)

# Formatting: You can prettify the output using the indent parameter:
json_string = json.dumps(data, indent=4)
print(json_string)
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }

# DECODING JSON to python - json.loads(): Parses a JSON string into a Python object (usually a dictionary or list).
json_string = '{"name": "Bob", "age": 25, "city": "London"}'

data = json.loads(json_string)
print(data["name"])

# Working with JSON Files - json.dump(): Writes Python data to a JSON file.
data = {"name": "Charlie", "age": 20}

with open("./data/json-test.json", "w") as file:
    json.dump(data, file, indent=4)

# json.load(): Reads JSON data from a file to a python dictionary.
with open("./data/json-test.json", "r") as file:
    data = json.load(file)
    print(type(data))
    print(data)

# convert dictionary and other types of python objects into JSON strings and print the values
# NOTE: they get converted to the JSON (JavaScript) equivalents:
# dict -> object, list -> Array, tuple -> Array, str -> String, int -> Number, float -> Number, True -> true, False -> false, None -> null
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# Use the separators parameter to change the default separator:
print(json.dumps(x, indent=4, separators=(". ", " = ")))

# Use the sort_keys parameter to specify if the result should be sorted or not:
print(json.dumps(x, indent=4, sort_keys=True))

