# Author: Gideo Komla Agbavor

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw the pattern using nested loops
while row < size:
    for _ in range(size):
        print("*", end=" ")
    print()  # Move to the next line after each row
    row += 1
