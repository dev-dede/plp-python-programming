my_list = []

my_list = [10, 20, 30, 40]
print(my_list)

my_list.insert(1, 15)
print(my_list)

new_list = [50, 60, 70]

my_list.extend(new_list)
print(my_list)

del my_list[-1]
print(my_list)

my_list.sort(reverse=True)
print(my_list)

print(my_list.index(30))
