def get_non_negative_integer():
    """Gets a non-negative integer input from the user."""

    # For simplicity, we're not doing full input validation here (no error handling)
    # Consider adding validation as an extra challenge
    num = int(input("Enter a non-negative integer: "))
    return num


def calculate_factorial(n):
    """Calculates the factorial of a non-negative integer."""

    if n == 0:
        factorial = 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
    
    return factorial


# Main program flow
number = get_non_negative_integer()
factorial = calculate_factorial(number)
print(f"The factorial of {number} is: {factorial}")