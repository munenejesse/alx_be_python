# Program to divide two numbers with exception handling

try:
    # Get input from the user
    numerator = float(input("Enter the first number (numerator): "))
    denominator = float(input("Enter the second number (denominator): "))

    # Perform division
    result = numerator / denominator

    # Display result
    print(f"The result of {numerator} divided by {denominator} is {result}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed. Please enter a non-zero denominator.")

except ValueError:
    print("Error: Please enter valid numbers.")
