def square_of_elements(input_list):
    squared_list = [num ** 2 for num in input_list]
    return squared_list

# Ask user for input
user_list = input("Enter a list of numbers").split()

# Convert the list elements to integers
user_list = [int(num) for num in user_list]

# Find squares of the elements
squared_elements = square_of_elements(user_list)

print("Squared elements:")
for element in squared_elements:
    print(element)
