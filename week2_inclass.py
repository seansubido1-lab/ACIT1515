# Create a variable named x and store an integer (whole number) inside it
x = 10

# Create a variable named y and store a string (any characters between single or double quotes) inside it
y = "20"

# Create a variable named z and store a float in it
z = "30.3"

# Change the value stored in the x variable to a new string
x = str(x)

# Change the value stored in the y variable to a new boolean
y = bool(y)

# Change the value store in the z variable to a different float
z = float(z)

# Print the value the user entered from the previous section
#skip!

# Print the (current) value of the variable x
print(x)

# Print the *type* (not the value itself) of the value stored in the y variable
print(type(y))

# Create two variables, one containing the string CIT, and another containing the string 1515
course = "ACIT"
number = "1515"

# Using the two variables and a hard-coded letter, print the word ACIT1515 to the terminal
course_number = f"{course}{number}"
print(course_number)