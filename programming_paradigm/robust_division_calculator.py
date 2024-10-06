
    # robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert inputs to float and attempt division
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            return "Error: Cannot divide by zero."
        result = numerator / denominator
        return f"The result of the division is {result}"
    
    except ValueError:
        # Handles non-numeric input
        return "Error: Please enter numeric values only."
