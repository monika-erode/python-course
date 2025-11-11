# Example data structures for contacts

# List: ordered, mutable collection
contacts = [
    {"name": "Asha", "phone": "99999 11111"},
    {"name": "Ravi", "phone": "88888 22222"}
]

# Tuple: ordered, immutable (use for constant coordinates)
office_location = (12.9716, 77.5946)  # latitude, longitude

# Dictionary: key-value pairs for quick lookup
phonebook = {"Asha": "99999 11111", "Ravi": "88888 22222"}

# Set: unordered, unique collection (for unique tags)
tags = {"friend", "coworker", "gym"}

# Add a new contact (list + dict)
new_contact = {"name": "Priya", "phone": "77777 33333"}
contacts.append(new_contact)
phonebook[new_contact["name"]] = new_contact["phone"]

# Lookup contact by name using dictionary (fast)
name_to_find = "Ravi"
if name_to_find in phonebook:
    print(f"{name_to_find}'s phone:", phonebook[name_to_find])

# Iterate contacts list
for contact in contacts:
    print(contact["name"], "-", contact["phone"])

# Demonstrate set uniqueness
tags.add("friend")  # duplicate, will not change the set
print("Tags:", tags)
