print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

ope = int(input("Enter choice 1,2,3 or 4 : "))

if ope in (1, 2, 3, 4):
    
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    if ope == 1:
        print(num1, "+", num2, "=", num1 + num2)
    elif ope == 2:
        print(num1, "-", num2, "=", num1 - num2)
    elif ope == 3:
        print(num1, "*", num2, "=", num1 * num2)
    elif ope == 4:
        print(num1, "/", num2, "=", num1 / num2)
else:
    print("Invalid Input")
