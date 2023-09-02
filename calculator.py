Number1 = int(input("Enter first number: "))
Number2 = int(input("Enter second number: "))
Operation = str(input("Choose the operation to be performed '+' to add, '-' to subtract '/' to divide and '*' to multiply: "))
Addition = Number1 + Number2
Subtraction = Number1 - Number2
Division = (Number1 / Number2)
Multiplication = Number1 * Number2
if Operation == '+':
    print("The sum is", Addition)
elif Operation == '-':
    print("The subtracted value is: ", Subtraction)
elif Operation == '/':
    print("The division is: ",Division)
elif Operation == '*':
    print("The multiplication answer is:", Multiplication)
else:
    print("Null operation value given")


