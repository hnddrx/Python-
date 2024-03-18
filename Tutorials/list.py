list = [[3, 2, 1, 4,4], [2,3], [3,2,4,1,6]]

list[0].append(5) #NOTE Append 5 into index 0
print(list)

for index in range(len(list)):
    list[index].sort() # Sort each list
    if index == 0 and index == 2:
        list[index].remove(0) #NOTE: Remove index 0 for list 0 and list 2
    

print(list)


