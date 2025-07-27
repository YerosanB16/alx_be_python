#!/usr/bin/env python3
# File: arithmetic_operations.py

def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

# Optional test cases
if __name__ == "__main__":
    print(perform_operation(10, 5, 'add'))       # ➝ 15
    print(perform_operation(10, 5, 'subtract'))  # ➝ 5
    print(perform_operation(10, 5, 'multiply'))  # ➝ 50
    print(perform_operation(10, 5, 'divide'))    # ➝ 2.0
    print(perform_operation(10, 0, 'divide'))    # ➝ Error: Cannot divide by zero
    print(perform_operation(10, 5, 'modulo'))    # ➝ Error: Invalid operation
