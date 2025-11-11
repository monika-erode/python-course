# Write
with open("cities.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")
    f.writelines(["This is Delhi\n", "This is Paris\n", "This is London\n"])

# Read whole file
with open("cities.txt", "r", encoding="utf-8") as f:
    contents = f.read()
    print("Full read:")
    print(contents)

# Read first 9 characters
with open("cities.txt", "r", encoding="utf-8") as f:
    print("First 9 chars:")
    print(f.read(9))
