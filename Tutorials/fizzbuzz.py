number = input('Number: ')
print(number)
"""     if (i % 15 == 0) console.log("FizzBuzz");
    else if (i % 3 == 0) console.log("Fizz");
    else if (i % 5 == 0) console.log("Buzz") """

if(int(number) % 3 == 0):
        print('Buzz')
elif(int(number) % 5 == 0):
        print('Fizz')
else:
        print('FizzBuzz1')
    
#Iterate every element ranging from 0 to 101
for index in range(1, 31):
    if index % 15 == 0:
        print(str(index) + ' ' + 'FizzBuzz') #NOTE: If the number is divisible by both 3 and 5 then it will print FizzBuzz
    elif index % 3 == 0:
        print(str(index) + ' ' + 'Fizz') #NOTE: If the number is divisible by 3 then it will print Fizz
    elif index % 5 == 0:
        print(str(index) + ' ' + 'Buzz') #NOTE: If the number is divisible by 3 then it will print Buzz
    else: 
        print(index) # Else it will only print the index
        
        

"""
OUTPUT: 
1
2
3 Fizz
4
5 Buzz
6 Fizz
7
8
9 Fizz
10 Buzz
11
12 Fizz
13
14
15 FizzBuzz
16
17
18 Fizz
19
20 Buzz
21 Fizz
22
23
24 Fizz
25 Buzz
26
27 Fizz
28
29
30 FizzBuzz
"""
