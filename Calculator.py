def smart_calculator():
    print(" Welcome to the Advanced Smart Calculator!")
    
    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Exponentiation (**)")
        print("7. Floor Division (//)")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '8':
            print("Thank you for using the Advanced Smart Calculator! 👋")
            break
        
        if choice not in {'1','2','3','4','5','6','7'}:
            print("Invalid choice! Please select a number between 1 and 8.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values only.")
            continue

        if choice == '1':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed!")
        elif choice == '5':
            if num2 != 0:
                result = num1 % num2
                print(f"Result: {num1} % {num2} = {result}")
            else:
                print("Error: Modulus by zero is not allowed!")
        elif choice == '6':
            result = num1 ** num2
            print(f"Result: {num1} ** {num2} = {result}")
        elif choice == '7':
            if num2 != 0:
                result = num1 // num2
                print(f"Result: {num1} // {num2} = {result}")
            else:
                print("Error: Floor division by zero is not allowed!")

# Run the calculator
smart_calculator()
