# Simple Calculator
def calculator():
    print("Welcome to the Simple Calculator!")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

  
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

 
    choice = input("Enter your choice (1/2/3/4): ")


    if choice == '1':
        result = num1 + num2
        print(f"The result of addition: {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"The result of subtraction: {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"The result of multiplication: {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of division: {result}")
        else:
            print("Error: Cannot divide by zero.")
    else:
        print("Invalid operation choice.")

calculator()
