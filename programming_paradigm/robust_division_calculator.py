def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        return num / denom
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Non-numeric input provided."