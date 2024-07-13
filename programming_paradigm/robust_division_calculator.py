class ZeroDivisionError(Exception):
    def __str__(self):
        print("Error: Cannot divide by zero.")


def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        raise ValueError("Error: Please enter numeric values only.")
    try:
        return numerator/denominator
    except:
        raise ZeroDivisionError
    finally:
        pass
