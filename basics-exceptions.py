try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["invalid_key"])
except FileNotFoundError as error_message:
    file = open("./data/a_file.txt", "w")
    print(f"Error: {error_message}. New file created")
except KeyError as error_message:
    print(f"ERROR: {error_message}")
else:  # block is executed only if there were no exceptions
    content = file.read()
    print(content)
finally:  # block is executed independent of whether there were exceptions
    file.close()
    print("File was closed")
    