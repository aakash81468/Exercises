def remove_duplicates(input_list):
    # Create an empty list
    unique_list = []

    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

# Ask user for input
user_list = input("Enter a list of elements").split()

# Remove duplicates
unique_ele = remove_duplicates(user_list)

# Print the list 
print("List with removed duplicates:")
print(unique_ele)
