# Mario Pyramid-builder program

height = input("Please enter height of pyramid above 0: ")

# Check for valid height number
try:
    height = int(height)
except:
    print("Please enter a valid integer")
    exit()

if 0 <= height:
    # Set pound signs and spaces for iteration in the loop
    pound = 1
    spaces = 1
    for num in range(0, height):
        print(" " * (height - 1)),  # Print spaces precluding hashes
        print("#" * (num + 1))  # Two hashes for start of pyramid
        height -= 1  # Subtracts one space for every iteration
else:
    print("Integer outside of valid range")
    exit()
# This is very stupid
