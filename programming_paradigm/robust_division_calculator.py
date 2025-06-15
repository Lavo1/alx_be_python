def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        
        return "Error: Please enter numeric values only."
        # programming_paradigm/main.py

from robust_division_calculator import safe_divide

if __name__ == "__main__":
    numerator = input("Enter numerator: ")
    denominator = input("Enter denominator: ")
    print(safe_divide(numerator, denominator))
