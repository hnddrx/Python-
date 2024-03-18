# Open the file in read mode
with open('python3.txt', 'r') as file:
    # Read the file line by line
    lines = file.readlines()

# Print each line of the file
for line in lines:
    print(line.strip())  # strip() removes any leading or trailing whitespace
