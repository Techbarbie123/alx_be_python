def calculator():
    
    num_1 = float(input("Enter the first number:"))
    num_2 = float(input("Enter the second number:"))
    operation = input("Choose the operation (+, -, *, /):")

    match operation:
        case "+":
            result = num_1 + num_2
        case "-":
            result = num_1 - num_2
        case '*':
                result = num_1 * num_2
        case '/':
                if num_2 == 0:
                    print("Error: Division by zero is not valid.")
                    return
                else:
                    result = num_1 / num_2
        case _:
          print("Invalid operation. Please choose from +, -, *, /.")        
    print(f"The result is {result}.")
    
calculator()