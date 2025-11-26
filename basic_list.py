
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

for num in range(len(my_list)):
    if my_list[num] not in new_list:
        new_list.append(my_list[num])
print("The list with unique elements only:")
print(new_list)