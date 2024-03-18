def readFile(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()  # Use readlines() to read all lines into a list
            # Print each line of the file
            for line in lines:
                print(line.strip())  # strip() removes any leading or trailing whitespace
    except FileNotFoundError:
        print("File not found!")
    except IOError: # NOTE: If there is any other input/output error (raises IOError), it prints "Error reading the file!".
        print("Error reading the file!")

def writeFile(input_text):
    global path # NOTE: Made this variable global using the global keyword so I can also use it outside this function
    path = 'python3-activity-WHM1.txt'
    try:
        # Open the file in write mode ('w')
        with open(path, 'w') as file:
            file.write(f"{input_text}\n")  # Corrected to add input_text without leading space
    except IOError: # NOTE: If there is any other input/output error (raises IOError), it prints "Error reading the file!".
        print("Error writing to the file!")

input_text = input('Write Here: ')
writeFile(input_text)
readFile(path)  # Call readFile() after writeFile()
