# pattern_drawing.py

# Prompt the user to enter a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Outer while loop for each row
while row < size:
    # Inner for loop for each column in the row
    for col in range(size):
        print("*", end="")  # Print * without newline
    print()  # Move to the next line after a row is complete
    row += 1
