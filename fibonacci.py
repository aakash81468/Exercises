def fibonacci_numbers(num):
    fibonacci_numbers = [0, 1] 

    for i in range(2, num):
        next_number = fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2]
        fibonacci_numbers.append(next_number)

    return fibonacci_numbers[:num]

# Ask user for input
num_of_numbers = int(input("How many Fibonacci numbers do you want to generate? "))

# Generate the Fibonacci numbers
fibonacci_sequence = fibonacci_numbers(num_of_numbers)

# Print generated Fibonacci numbers
print("Generated Fibonacci sequence:")
for number in fibonacci_sequence:
    print(number)
