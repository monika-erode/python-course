import json

person = {
    "name": "Hari",
    "age": 22,
    "skills": ["Python", "React", "AWS"]
}

with open("data.json", "w") as file:
    json.dump(person, file, indent=4)

print("Data saved to JSON!")
