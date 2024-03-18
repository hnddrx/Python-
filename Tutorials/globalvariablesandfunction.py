#This is a function in python that gets the global variable
"""
The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
"""

thisIsAString = "Hello, World!" #This is a global variable
def getGlobalVariable():
        global fromFunction #use the global keyword if you want to change a global variable inside a function.
        fromFunction = "This is from function"
        fromThisFunction = "This is not a global variable from this funciton"
        thisIsAString = "That's fantastic" #This is a local variable of this function
        print("The first phrase I've wrote in python is " + "'" + thisIsAString + "'")
getGlobalVariable()

print("Phrase: " + thisIsAString) #This print the value of the global variable thisIsAString with the value of a strint 'Hello, World!'
print(fromFunction) #This variable is from the function that is globalized using the global keyword


