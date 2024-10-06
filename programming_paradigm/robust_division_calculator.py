def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
    except ZeroDivisionError:
        return "invalid division input."
    except ValueError:
        return "error!, please enter a valid numeric number."
    