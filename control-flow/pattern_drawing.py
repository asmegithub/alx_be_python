# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Draw the Pattern
row = 1
while row <= size:
    col = 1
    while col <= size:
        print("*", end="")
        col += 1
    print()
    row += 1