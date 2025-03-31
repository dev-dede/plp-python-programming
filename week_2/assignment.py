my_list = []

my_list = [10, 20, 30, 40] #Can use .append to append one after the other
print(my_list)

my_list.insert(1, 15)
print(my_list)

my_list.extend([50, 60, 70]) #Directly put the list in the function
print(my_list)

del my_list[-1] #Could also use my_list.pop() to specifically remove the last item
print(my_list)

my_list.sort(reverse=True) #Decided to sort in descending order since list is already in ascending order
print(my_list)

print(my_list.index(30))
