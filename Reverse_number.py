def reverse_number(number):
    reversed_number = 0

    while number > 0:
        last_digit = number % 10
        reversed_number = (reversed_number * 10) + last_digit
        number = number // 10

    return reversed_number

# Ask user for input
user_num = int(input("Enter a number: "))

# Find reverse of the number
reversed_number = reverse_number(user_num)

print("Reversed number:", reversed_number)
