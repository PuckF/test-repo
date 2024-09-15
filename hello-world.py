import json

def write_json(filename, contents):
    # Writing data to the JSON file
    with open(filename, 'w') as file:
        json.dump(contents, file, indent=4)

# Define the data to be written to the JSON file in dictionary format
data = {
    "members": [
        {"name": "Harry Potter", "age": 11, "occupation": "Student"},
        {"name": "Albus Dumbledore", "age": 110, "occupation": "Headmaster"},
        {"name": "Minerva McGonagall", "age": 88, "occupation": "Professor"}
    ],
    "school": "Hogwarts",
    "location": "Schotland"
}

filename = "example_data.json"

write_json(filename, data)

###########################################

def read_json(filename):
    # Reading data from the JSON file
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

data = read_json("example_data.json")

# Print the entire file
print("Data read from the JSON file:")
print(data)

# Access specific parts of the data
print("School Name:", data["school"])
print("Location:", data["location"])

# Iterate through the list of members
print("Members:")
for member in data["members"]:
    print(f"Name: {member['name']}, Age: {member['age']}, Occupation: {member['occupation']}")