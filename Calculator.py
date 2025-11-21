def smart_calculator():
    print("Welcome to the Smart Calculator!")
    
    # Take user input for numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values only.")
        return

    # Perform calculations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    
    # Handle division by zero
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Undefined (division by zero is not allowed)"

    # Display results
    print("\nResults:")
    print(f"{num1} + {num2} = {addition}")
    print(f"{num1} - {num2} = {subtraction}")
    print(f"{num1} * {num2} = {multiplication}")
    print(f"{num1} / {num2} = {division}")

# Call the function
smart_calculator()
