# Initialize variables
total = 0
mark = 0
# Repeat the loop until mark == -1
while mark != -1:
    # Prompt for a new mark value
    mark = int(input("Enter value for mark, -1 to finish: "))

    if mark != -1:
        total += mark

print("Total:", total)

###

num = int(input("Enter a number: "))
while num != 0:
    num = int(input("Enter a number: "))

