def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2  
    elif operation == 'subtract':
<<<<<<< HEAD
        return num1 - num2
=======
        return num1 -num2
>>>>>>> 806777b8883a9cb8a22306f7e8e75df19627561c
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "error!",  "division by zero"
        return num1 / num2
    else:
        return "error!", "operation is not valid"
    
    
