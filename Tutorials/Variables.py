#Variables do not need to be declared with any particular type, and can even change type after they have been set.
#Example:
#NOTE: This will create two variables
thisIsAnInteger = 5 # int 
ThisIsAnInteger = "Five"


#NOTE: String variables can be declared either by using single or double quotes:
thisIsAString = 'Hello, World!' # str using single string NOTE this variable will be a global variable
thisIsAnotherString = "Hello, World!!" # str using double string

#NOTE: Get the type of the variable using type() function
print(type(thisIsAnInteger))
print(type(thisIsAString))


#NOTE: Assigning multiple values in at once
x,y,z = 'Orange', 'Red', "Blue"
print(x)
print(y)
print(z)

#NOTE: Assigning single value into multiple variables
X = Y = Z = "Orange"

#NOTE: The Python print() function is often used to output variables.
print(X,Y,Z) #In the print() function, you output multiple variables, separated by a comma:

#Assigning array/list  into  variables
first, second, third = ["Orange", "Red", "Green"]
print(first, second, third)

#Assigning lists into variables
first = second = third = ["Orange", "Red", "Green"]
print(first, second, third)
print(first + second + third) #You can also use the + operator to output multiple variables:
for element in first: #for every element in str first 
        print(element)
