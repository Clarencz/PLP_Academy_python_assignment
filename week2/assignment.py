# Create an empty list called my_list.
my_list =[]

# Append the following elements to my_list: 10, 20, 30, 40.
my_list2 = 10,20,30,40

# my_list.append([10,20,30,40])

for _ in my_list2:
    my_list.append(_)
print(my_list)

# my_list+=my_list2


# Insert the value 15 at the second position in the list.
# my_list[0][1]=15
my_list[1] = 15

# Extend my_list with another list: [50, 60, 70].
my_list.extend([50,60,70])

# Remove the last element from my_list.
my_list.pop()

# Sort my_list in ascending order.
my_list.sort()

# Find and print the index of the value 30 in my_list.
print(my_list)